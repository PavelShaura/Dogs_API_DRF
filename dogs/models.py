from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Breed(models.Model):
    """
    Модель, представляющая породу собаки.

    Attributes:
        name (str): Название породы.
        size (str): Размер породы ('Tiny', 'Small', 'Medium', 'Large').
        friendliness (int): Оценка дружелюбия породы (от 1 до 5).
        trainability (int): Оценка обучаемости породы (от 1 до 5).
        shedding_amount (int): Оценка количества линьки (от 1 до 5).
        exercise_needs (int): Оценка потребности в физических упражнениях (от 1 до 5).
    """

    DOG_SIZE = [
        ('Tiny', _('Tiny')), ('Small', _('Small')), ('Medium', _('Medium')), ('Large', _('Large'))
    ]

    name = models.CharField(_('name'), max_length=100)
    size = models.CharField(_('size'), max_length=10, choices=DOG_SIZE)
    friendliness = models.IntegerField(_('friendliness'), choices=[(i, i) for i in range(1, 6)])
    trainability = models.IntegerField(_('trainability'), choices=[(i, i) for i in range(1, 6)])
    shedding_amount = models.IntegerField(_('shedding amount'), choices=[(i, i) for i in range(1, 6)])
    exercise_needs = models.IntegerField(_('exercise needs'), choices=[(i, i) for i in range(1, 6)])

    class Meta:
        verbose_name = _('breed')
        verbose_name_plural = _('breeds')

    def __str__(self):
        return self.name


class Dog(models.Model):
    """
    Модель, представляющая собаку.

    Attributes:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        gender (str): Пол собаки.
        color (str): Окрас собаки.
        favorite_food (str): Любимая еда собаки.
        favorite_toy (str): Любимая игрушка собаки.
        breed (Breed): Порода собаки.
    """

    name = models.CharField(_('name'), max_length=100)
    age = models.IntegerField(_('age'))
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs', verbose_name=_('breed'))
    gender = models.CharField(_('gender'), max_length=10)
    color = models.CharField(_('color'), max_length=50)
    favorite_food = models.CharField(_('favorite food'), max_length=100)
    favorite_toy = models.CharField(_('favorite toy'), max_length=100)

    class Meta:
        verbose_name = _('dog')
        verbose_name_plural = _('dogs')

    def __str__(self):
        return self.name
