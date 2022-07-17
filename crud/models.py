from django.db import models
from django.urls import reverse

# Create your models here.


class Land(models.Model):

    name = models.CharField(max_length=30, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('land_detail', args=[str(self.id)])


class User(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    Password = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Farmers(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    discreption = models.CharField(max_length=200, blank=True, null=True)
    cost_per_hour = models.IntegerField(blank=True, null=True)
    farmer_land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('farmer_list')


class Plant(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    seed_cost = models.IntegerField(blank=True, null=True)
    plant_land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant_list')


class Fertilizer(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    fertilizer_plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE, blank=True, null=True
    )
    fertilizer_land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fertilizer_list')


class Pesticides(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, blank=True, null=True)
    pesticide_land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pesticide_list')


class Disease(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    disease_plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('disease_list')


class Medicine(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    disease = models.ForeignKey(
        Disease, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('medicine_list')


class TCost(models.Model):
    total_cost = models.IntegerField(blank=True, null=True)
    water_cost = models.IntegerField(blank=True, null=True)
    medicine_cost = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, blank=True, null=True)
    seed_cost = models.ForeignKey(
        Plant, on_delete=models.CASCADE, blank=True, null=True)
    labor_cost = models.ForeignKey(
        Farmers, on_delete=models.CASCADE, blank=True, null=True)
    pesticides_cost = models.ForeignKey(
        Pesticides, on_delete=models.CASCADE, blank=True, null=True)
    fertilizer_cost = models.ForeignKey(
        Fertilizer, on_delete=models.CASCADE, blank=True, null=True)
    land_name = models.ForeignKey(
        Land, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.land_name.name


class Sales(models.Model):
    crop_weight = models.IntegerField(blank=True, null=True)
    sale_price = models.IntegerField(blank=True, null=True)
    land_name = models.ForeignKey(
        Land, on_delete=models.CASCADE, blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.land_name.name

    def get_absolute_url(self):
        return reverse('cost_template')
