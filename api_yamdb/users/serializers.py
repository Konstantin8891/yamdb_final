from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.core.mail import send_mail

from rest_framework.serializers import ModelSerializer, CharField, EmailField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser
from api.utils import get_check_hash


class UserCreateSerializer(ModelSerializer):

    class Meta():
        fields = (
            'email',
            'username',
        )
        model = CustomUser

    def create(self, validated_data):
        """
        Создать и вернуть нового CustomUser если данные валидные.
        """
        new_user = CustomUser.objects.create(**validated_data)
        username = new_user.username
        email = new_user.email
        code = get_check_hash.make_token(new_user)
        send_mail(
            from_email='from@example.com',
            subject=f'Hello, {username} Confirm your email',
            message=f'Your confirmation code: {code}.',
            recipient_list=[
                email,
            ],
            fail_silently=False,
        )
        return new_user


class UsersSerializer(ModelSerializer):

    class Meta():
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        model = CustomUser

    def validate_password(self, value: str) -> str:
        """
        Захешировать пустой пароль.
        """
        return make_password(value)


class UserSelfSerializer(UsersSerializer):
    username = CharField(
        max_length=150,
        required=False,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message="""This value may contain only letters,
                digits and @/./+/-/_ characters."""
            ),
            RegexValidator(
                regex=r'^\b(m|M)e\b',
                inverse_match=True,
                message="""Username Me registration not allowed."""
            )
        ],
    )
    email = EmailField(
        required=False,
        max_length=255
    )
    role = CharField(read_only=True)


class UserKeySerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = CharField(required=True)
        self.fields['password'].required = False
        self.fields['confirmation_code'] = CharField(required=True)

    def validate(self, attrs):
        attrs.update({'password': ''})
        return super(UserKeySerializer, self).validate(attrs)
