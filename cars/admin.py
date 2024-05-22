from django.contrib import admin

from cars.models import Brand, Vehicle


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("vehicle_model", "brand", "year", "fuel_type" ,"license_plate")
    search_fields = ("vehicle_model", "brand", "fuel_type")
    list_filter = ("brand", "fuel_type", "number_of_doors", "transmission")


admin.site.register(Brand, BrandAdmin)
admin.site.register(Vehicle, VehicleAdmin)
