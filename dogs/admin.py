from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Breed, Dog, User


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    )
    list_filter = (
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    )
    search_fields = ("name",)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "breed", "gender", "color")
    list_filter = ("breed", "gender")
    search_fields = ("name", "breed__name")
    raw_id_fields = ("breed",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
