from typing import Any

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления отдельной собаки.

    Attributes:
        queryset (QuerySet): Queryset для модели Dog.
        serializer_class (DogSerializer): Сериализатор для модели Dog.
        http_method_names (list): Список разрешенных HTTP-методов.
    """

    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    http_method_names = ["get", "put", "delete"]

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.retrieve(request, *args, **kwargs)
        except NotFound:
            return Response(
                {"error": "Dog not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.update(request, *args, **kwargs)
        except NotFound:
            return Response(
                {"error": "Dog not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            self.destroy(request, *args, **kwargs)
            return Response(
                {"status": "Dog deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        except NotFound:
            return Response(
                {"error": "Dog not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DogList(generics.ListCreateAPIView):
    """
    Представление для получения списка собак и создания новой собаки.

    Attributes:
        queryset (QuerySet): Queryset для модели Dog.
        serializer_class (DogSerializer): Сериализатор для модели Dog.
    """

    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления отдельной породы.

    Attributes:
        queryset (QuerySet): Queryset для модели Breed.
        serializer_class (BreedSerializer): Сериализатор для модели Breed.
        http_method_names (list): Список разрешенных HTTP-методов.
    """

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ["get", "put", "delete"]

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.retrieve(request, *args, **kwargs)
        except NotFound:
            return Response(
                {"error": "Breed not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.update(request, *args, **kwargs)
        except NotFound:
            return Response(
                {"error": "Breed not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            self.destroy(request, *args, **kwargs)
            return Response(
                {"status": "Breed deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        except NotFound:
            return Response(
                {"error": "Breed not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BreedList(generics.ListCreateAPIView):
    """
    Представление для получения списка пород и создания новой породы.

    Attributes:
        queryset (QuerySet): Queryset для модели Breed.
        serializer_class (BreedSerializer): Сериализатор для модели Breed.
    """

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            return self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
