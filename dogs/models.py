from django.contrib.auth.models import AbstractUser
from django.db import models


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
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=DOG_SIZE)
    friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    trainability = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    shedding_amount = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    exercise_needs = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

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

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="dogs")

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name
