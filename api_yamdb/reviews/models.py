from django.db import models

from users.models import CustomUser


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='titles',
        blank=True, null=True
    )
    genre = models.ManyToManyField(
        Genre, related_name='titles', blank=True
    )

    def get_genres(self):
        return "\n".join([g.genres for g in self.genre.all()])


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        'Рейтинг',
        default=10
    )


class Review(models.Model):
    CHOICES = (
        (1, 'один'),
        (2, 'два'),
        (3, 'три'),
        (4, 'четыре'),
        (5, 'пять'),
        (6, 'шесть'),
        (7, 'семь'),
        (8, 'восемь'),
        (9, 'девять'),
        (10, 'десять')
    )

    text = models.TextField(
        'Текст отзыва',
        help_text='Введите текст отзыва'
    )
    score = models.PositiveSmallIntegerField(
        choices=CHOICES,
        help_text='Оцените произведение'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='review'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    text = models.TextField(
        'Текст коммента',
        help_text='Введите коммент'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
