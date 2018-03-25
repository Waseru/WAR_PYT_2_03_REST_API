from django.contrib import admin
# Register your models here.
from .models import Person, Movie, Role

class RoleInline(admin.TabularInline):
    model = Role
    extra = 1

@admin.register(Person)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        RoleInline,
    ]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [
        RoleInline,
    ]
    exclude = ('actor',)


# admin.site.register(Person)
# admin.site.register(Movie)


