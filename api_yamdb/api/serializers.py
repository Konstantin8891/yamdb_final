from django.db.models import Avg

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    SlugRelatedField
)

from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Genre


class TitleSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = SerializerMethodField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )

    def get_rating(self, obj):
        rate = Review.objects.filter(title_id=obj.id).aggregate(Avg('score'))
        for rating in rate.values():
            if rating:
                return int(rating)


class TitlePostSerializer(ModelSerializer):
    genre = SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genre.objects.all()
    )
    category = SlugRelatedField(
        slug_field='slug',
        many=False,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category'
        )


class ReviewSerializer(ModelSerializer):

    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date',
        )
        model = Review


class CommentSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)
    review = StringRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
