from rest_framework import serializers
from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Breed."""

    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
        ]


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Dog."""

    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source="breed", queryset=Breed.objects.all()
    )

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "breed_id",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        ]
