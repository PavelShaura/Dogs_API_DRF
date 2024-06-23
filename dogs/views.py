from typing import Any

from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response

from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer


class DogDetail(APIView):
    """
    Представление для получения, обновления и удаления отдельной собаки.
    """

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            dog = Dog.objects.get(pk=kwargs["pk"])
            serializer = DogSerializer(dog)
            return Response(serializer.data)
        except Dog.DoesNotExist:
            return Response(
                {"error": _("Dog not found")}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            dog = Dog.objects.get(pk=kwargs["pk"])
            serializer = DogSerializer(dog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Dog.DoesNotExist:
            return Response(
                {"error": _("Dog not found")}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            dog = Dog.objects.get(pk=kwargs["pk"])
            dog.delete()
            return Response(
                {"status": _("Dog deleted")}, status=status.HTTP_204_NO_CONTENT
            )
        except Dog.DoesNotExist:
            return Response(
                {"error": _("Dog not found")}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DogViewSet(viewsets.ModelViewSet):
    """
    Представление для получения списка собак и создания новой собаки.
    """

    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    http_method_names = ["get", "post"]

    def list(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):
    """
    Представление для получения, обновления и удаления отдельной породы.
    """

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            breed = Breed.objects.get(pk=kwargs["pk"])
            serializer = BreedSerializer(breed)
            return Response(serializer.data)
        except Breed.DoesNotExist:
            return Response(
                {"error": _("Breed not found")}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            breed = Breed.objects.get(pk=kwargs["pk"])
            serializer = BreedSerializer(breed, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Breed.DoesNotExist:
            return Response(
                {"error": _("Breed not found")}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            breed = Breed.objects.get(pk=kwargs["pk"])
            breed.delete()
            return Response(
                {"status": _("Breed deleted")}, status=status.HTTP_204_NO_CONTENT
            )
        except Breed.DoesNotExist:
            return Response(
                {"error": _("Breed not found")}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BreedViewSet(viewsets.ModelViewSet):
    """
    Представление для получения списка пород и создания новой породы.
    """

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ["get", "post"]

    def list(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
