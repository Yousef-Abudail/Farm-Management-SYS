from django import forms
from .models import Land,Plant,Farmers,Disease,Sales

class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = [
            "name",
            "size",
        ]


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields =['name',
        'seed_cost',
        'plant_land'
        ]

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmers
        fields = ['name',
        'discreption',
        'cost_per_hour',
        'farmer_land'
        ]

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name',
        'disease_plant'
        ]


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['sale_price']