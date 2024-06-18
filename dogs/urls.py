from django.urls import path
from dogs.views import DogDetail, DogList, BreedDetail, BreedList

urlpatterns = [
    path("dogs/<int:pk>/", DogDetail.as_view(), name="dog-detail"),
    path("dogs/", DogList.as_view(), name="dog-list"),
    path("breeds/<int:pk>/", BreedDetail.as_view(), name="breed-detail"),
    path("breeds/", BreedList.as_view(), name="breed-list"),
]
