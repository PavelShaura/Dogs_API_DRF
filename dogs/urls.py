from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dogs.views import DogDetail, DogViewSet, BreedDetail, BreedViewSet

router = DefaultRouter()
router.register(r"dogs", DogViewSet)
router.register(r"breeds", BreedViewSet)

urlpatterns = [
    path("dogs/<int:pk>/", DogDetail.as_view(), name="dog-detail"),
    path("breeds/<int:pk>/", BreedDetail.as_view(), name="breed-detail"),

    path("", include(router.urls)),
]
