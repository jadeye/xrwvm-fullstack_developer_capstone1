from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms to display

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year', 'color', 'price', 'dealer_id')
    list_filter = ('car_make', 'car_type', 'year')
    search_fields = ('name', 'car_make__name')

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
