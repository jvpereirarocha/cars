from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(verbose_name='Brand ID', primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Brand name')

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = [["brand_id", "name"]]
        indexes = [
            models.Index(
                fields=["brand_id", "name"],
                name="brand_id_name_idx"
            )
        ]


class Vehicle(models.Model):
    TYPES_OF_TRANSMISSIONS = [
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
    ]
    FUEL_TYPES = [
        ("Gasoline", "Gasoline"),
        ("Diesel", "Diesel"),
        ("Alcohol", "Alcohol"),
    ]

    vehicle_id = models.AutoField(verbose_name="Vehicle ID", primary_key=True)
    vehicle_model = models.CharField(verbose_name="Vehicle model", max_length=200)
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT, related_name="vehicle_brand", related_query_name="brand")
    license_plate = models.CharField(verbose_name="License Plate", max_length=20)
    year = models.IntegerField(verbose_name="Year")
    transmission = models.CharField(verbose_name="Transmission", choices=TYPES_OF_TRANSMISSIONS)
    fuel_type = models.CharField(verbose_name="Fuel type", choices=FUEL_TYPES)
    number_of_doors = models.IntegerField(verbose_name="Number of doors")
    image = models.ImageField(verbose_name="Vehicle image", upload_to="upload/%d/%m/%Y/", null=True, blank=True, height_field=300, width_field=300)

    def __str__(self) -> str:
        return f"{self.vehicle_model} - {self.year}"
    
    class Meta:
        unique_together = [["vehicle_model", "year"]]
        constraints = [
            models.CheckConstraint(check=models.Q(year__gte=1920), name="year_gte_1920")
        ]
        indexes = [
            models.Index(
                fields=["vehicle_model", "year"],
                name="model_year_idx"
            ),
            models.Index(
                fields=["year", "brand"],
                name="year_brand_idx"
            ),
            models.Index(
                fields=["vehicle_model", "year", "brand"],
                name="model_year_brand_idx"
            ),
            models.Index(
                fields=["year", "brand", "fuel_type"],
                name="year_brand_fueltype_idx"
            ),
            models.Index(
                fields=["year", "transmission", "fuel_type"],
                name="year_transmission_fueltype_idx"
            ),
        ]
