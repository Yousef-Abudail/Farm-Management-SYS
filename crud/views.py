from ast import Global
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.views import View
from .models import Disease, Land, TCost, Farmers, Plant, Fertilizer, Pesticides, Medicine, Sales
from .forms import SalesForm

'''Landing page view'''


class WelcomePage(TemplateView):
    template_name = 'landing_page/startbootstrap-freelancer-gh-pages/index.html'


'''Land Views'''


class LandCreate(CreateView):
    model = Land
    fields = ['name', 'size']
    template_name = 'land_crud/land_creat.html'


class LandDetailView(DetailView):
    model = Land
    fields = ['name', 'size']
    template_name = 'land_crud/land_detail.html'


class LandListView(ListView):
    model = Land
    fields = ['name', 'size']
    template_name = 'land_crud/land_list.html'


class LandUpdateView(UpdateView):
    model = Land
    fields = ['name', 'size']
    template_name = 'land_crud/land_update.html'


class LandDeleteView(DeleteView):
    model = Land
    fields = ['name', 'size']
    template_name = 'land_crud/land_delete.html'
    success_url = reverse_lazy('land_list')


'''Plant Views'''


class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'seed_cost', 'plant_land']
    template_name = 'plant_crud/plant_creat.html'


class PlantListView(ListView):
    model = Plant
    fields = ['name', 'seed_cost', 'plant_land']
    template_name = 'plant_crud/plant_list.html'


class PlantUpdateView(UpdateView):
    model = Plant
    fields = ['name', 'seed_cost', 'plant_land']
    template_name = 'plant_crud/plant_update.html'


class PlantDeleteView(DeleteView):
    model = Plant
    fields = ['name', 'seed_cost', 'plant_land']
    template_name = 'plant_crud/plant_delete.html'
    success_url = reverse_lazy('plant_list')


'''Farmer Views'''


class FarmerCreate(CreateView):
    model = Farmers
    fields = ['name', 'discreption', 'cost_per_hour', 'farmer_land']
    template_name = 'farmer_crud/farmer_creat.html'


class FarmerListView(ListView):
    model = Farmers
    fields = ['name', 'discreption', 'cost_per_hour', 'farmer_land']
    template_name = 'farmer_crud/farmer_list.html'


class FarmerUpdateView(UpdateView):
    model = Farmers
    fields = ['name', 'discreption', 'cost_per_hour', 'farmer_land']
    template_name = 'farmer_crud/farmer_update.html'


class FarmerDeleteView(DeleteView):
    model = Farmers
    fields = ['name', 'discreption', 'cost_per_hour', 'farmer_land']
    template_name = 'farmer_crud/farmer_delete.html'
    success_url = reverse_lazy('farmer_list')


'''Disease Views'''


class DiseaseCreate(CreateView):
    model = Disease
    fields = ['name', 'disease_plant']
    template_name = 'disease_crud/disease_creat.html'


class DiseaseListView(ListView):
    model = Disease
    fields = ['name', 'disease_plant']
    template_name = 'disease_crud/disease_list.html'


class DiseaseUpdateView(UpdateView):
    model = Disease
    fields = ['name', 'disease_plant']
    template_name = 'disease_crud/disease_update.html'


class DiseaseDeleteView(DeleteView):
    model = Disease
    fields = ['name', 'disease_plant']
    template_name = 'disease_crud/disease_delete.html'
    success_url = reverse_lazy('disease_list')


'''Fertilizer Views'''


class FertilizerCreate(CreateView):
    model = Fertilizer
    fields = ['name', 'fertilizer_plant', 'fertilizer_land', 'cost']
    template_name = 'fertilizer_crud/fertilizer_creat.html'


class FertilizerListView(ListView):
    model = Fertilizer
    fields = ['name', 'fertilizer_plant', 'fertilizer_land', 'cost']
    template_name = 'fertilizer_crud/fertilizer_list.html'


class FertilizerUpdateView(UpdateView):
    model = Fertilizer
    fields = ['name', 'fertilizer_plant', 'fertilizer_land', 'cost']
    template_name = 'fertilizer_crud/fertilizer_update.html'


class FertilizerDeleteView(DeleteView):
    model = Fertilizer
    fields = ['name', 'fertilizer_plant', 'fertilizer_land', 'cost']
    template_name = 'fertilizer_crud/fertilizer_delete.html'
    success_url = reverse_lazy('fertilizer_list')


'''Medicine Views'''


class MedicineCreate(CreateView):
    model = Medicine
    fields = ['name', 'disease', 'cost']
    template_name = 'medicine_crud/medicine_creat.html'


class MedicineListView(ListView):
    model = Medicine
    fields = ['name', 'disease', 'cost']
    template_name = 'medicine_crud/medicine_list.html'


class MedicineUpdateView(UpdateView):
    model = Medicine
    fields = ['name', 'disease', 'cost']
    template_name = 'medicine_crud/medicine_update.html'


class MedicineDeleteView(DeleteView):
    model = Medicine
    fields = ['name', 'disease', 'cost']
    template_name = 'medicine_crud/medicine_delete.html'
    success_url = reverse_lazy('medicine_list')


'''Pesticides Views'''


class PesticidesCreate(CreateView):
    model = Pesticides
    fields = ['name', 'plant', 'cost', 'pesticide_land']
    template_name = 'pesticide_crud/pesticide_creat.html'


class PesticidesListView(ListView):
    model = Pesticides
    fields = ['name', 'plant', 'cost', 'pesticide_land']
    template_name = 'pesticide_crud/pesticide_list.html'


class PesticidesUpdateView(UpdateView):
    model = Pesticides
    fields = ['name', 'plant', 'cost', 'pesticide_land']
    template_name = 'pesticide_crud/pesticide_update.html'


class PesticidesDeleteView(DeleteView):
    model = Pesticides
    fields = ['name', 'plant', 'cost', 'pesticide_land']
    template_name = 'pesticide_crud/pesticide_delete.html'
    success_url = reverse_lazy('pesticide_list')


'''Sales Views'''


class SalesCreate(CreateView):
    model = Sales
    fields = ['crop_weight', 'sale_price', 'land_name', 'revenue']
    template_name = 'sales_crud/sales_creat.html'


class SalesListView(ListView):
    model = Sales
    fields = ['crop_weight', 'sale_price', 'land_name', 'revenue']
    template_name = 'sales_crud/sales_list.html'


class SalesUpdateView(UpdateView):
    model = Sales
    fields = ['crop_weight', 'sale_price', 'land_name', 'revenue']
    template_name = 'sales_crud/sales_update.html'
    success_url = reverse_lazy('sales_crud/sales_list')


class SalesDeleteView(DeleteView):
    model = Sales
    fields = ['crop_weight', 'sale_price', 'land_name', 'revenue']
    template_name = 'sales_crud/sales_delete.html'
    success_url = reverse_lazy('sales_crud/sales_list')


'''Home table view'''


def tableview(request):
    lands = Land.objects.all()
    tabel_dict = {}

    for land in lands:
        farmers = Farmers.objects.filter(farmer_land=land)[0]
        plants = Plant.objects.filter(plant_land=land)[0]
        fertilizer = Fertilizer.objects.filter(fertilizer_land=land)[0]
        pesticides = Pesticides.objects.filter(pesticide_land=land)[0]

        tabel_dict[land.name] = {'farmers': farmers,
                                 'plants': plants,
                                 'fertilizer': fertilizer,
                                 'pesticides': pesticides,
                                 }

    return render(request, 'home.html', {'tabel_dict': tabel_dict})


'''Selling price form view'''


def saleprice(request):
    global form

    form = SalesForm(request.POST)
    return render(request, 'cost_list.html', {'form': form})


'''Total cost view'''


def TCostview(request):
    costs = TCost.objects.all()

    cost_dict = {}
    for cost in costs:

        land_name = cost.land_name
        water_cost = cost.water_cost
        seed_cost = cost.seed_cost.seed_cost
        medicine_cost = cost.medicine_cost.cost
        labor_cost = cost.labor_cost.cost_per_hour
        pesticides_cost = cost.pesticides_cost.cost
        fertilizer_cost = cost.fertilizer_cost.cost

        global total_cost
        total_cost = (cost.water_cost
                      + cost.seed_cost.seed_cost
                      + cost.medicine_cost.cost
                      + cost.labor_cost.cost_per_hour
                      + cost.pesticides_cost.cost
                      + cost.fertilizer_cost.cost)

        cost_dict[land_name] = {
            "water_cost": water_cost,
            "seed_cost": seed_cost,
            "medicine_cost": medicine_cost,
            "labor_cost": labor_cost,
            "pesticides_cost": pesticides_cost,
            "fertilizer_cost": fertilizer_cost,
            "total_cost": total_cost,

        }

    return render(request, 'cost_list.html', {'cost_dict': cost_dict})
