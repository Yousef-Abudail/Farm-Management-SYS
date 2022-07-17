from django.urls import path
from .views import TCostview, tableview, saleprice
from .views import LandCreate, LandDetailView, LandListView, LandUpdateView, LandDeleteView
from .views import PlantCreate, PlantListView, PlantUpdateView, PlantDeleteView
from .views import FarmerCreate, FarmerListView, FarmerUpdateView, FarmerDeleteView
from .views import DiseaseCreate, DiseaseListView, DiseaseUpdateView, DiseaseDeleteView
from .views import FertilizerCreate, FertilizerListView, FertilizerUpdateView, FertilizerDeleteView
from .views import MedicineCreate, MedicineListView, MedicineUpdateView, MedicineDeleteView
from .views import PesticidesCreate, PesticidesListView, PesticidesUpdateView, PesticidesDeleteView
from .views import SalesCreate, SalesListView, SalesUpdateView, SalesDeleteView
from .views import WelcomePage

urlpatterns = [
    # Tcost Urls
    path('price/', saleprice, name='price'),
    path('cost/list/', TCostview, name='cost_list'),

    # Sales Urls
    path('sales/new/', SalesCreate.as_view(), name='sales_creat'),
    path('sales/list/', SalesListView.as_view(), name='sales_list'),
    path('sales/update/<int:pk>/', SalesUpdateView.as_view(), name='sales_update'),
    path('sales/delete/<int:pk>/', SalesDeleteView.as_view(), name='sales_delete'),
    
    # Pesticides Urls
    path('pesticide/new/', PesticidesCreate.as_view(), name='pesticide_creat'),
    path('pesticide/list/', PesticidesListView.as_view(), name='pesticide_list'),
    path('pesticide/update/<int:pk>/',
         PesticidesUpdateView.as_view(), name='pesticide_update'),
    path('pesticide/delete/<int:pk>/',
         PesticidesDeleteView.as_view(), name='pesticide_delete'),
    
    # Medicine Urls
    path('medicine/new/', MedicineCreate.as_view(), name='medicine_creat'),
    path('medicine/list/', MedicineListView.as_view(), name='medicine_list'),
    path('medicine/update/<int:pk>/',
         MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine/delete/<int:pk>/',
         MedicineDeleteView.as_view(), name='medicine_delete'),
    
    # Fertilizer Urls
    path('fertilizer/new/', FertilizerCreate.as_view(), name='fertilizer_creat'),
    path('fertilizer/list/', FertilizerListView.as_view(), name='fertilizer_list'),
    path('fertilizer/delete/<int:pk>/',
         FertilizerDeleteView.as_view(), name='fertilizer_delete'),
    path('fertilizer/update/<int:pk>/',
         FertilizerUpdateView.as_view(), name='fertilizer_update'),
    
    # Disease Urls
    path('disease/new/', DiseaseCreate.as_view(), name='disease_creat'),
    path('disease/list/', DiseaseListView.as_view(), name='disease_list'),
    path('disease/delete/<int:pk>/',
         DiseaseDeleteView.as_view(), name='disease_delete'),
    path('disease/update/<int:pk>/',
         DiseaseUpdateView.as_view(), name='disease_update'),
    
    # Farmers Urls
    path('farmer/new/', FarmerCreate.as_view(), name='farmer_creat'),
    path('farmer/list/', FarmerListView.as_view(), name='farmer_list'),
    path('farmer/delete/<int:pk>/',
         FarmerDeleteView.as_view(), name='farmer_delete'),
    path('farmer/update/<int:pk>/',
         FarmerUpdateView.as_view(), name='farmer_update'),
    
    # Plant Urls
    path('plant/new/', PlantCreate.as_view(), name='plant_creat'),
    path('plant/list/', PlantListView.as_view(), name='plant_list'),
    path('plant/delete/<int:pk>/', PlantDeleteView.as_view(), name='plant_delete'),
    path('plant/update/<int:pk>/', PlantUpdateView.as_view(), name='plant_update'),
    
    # Land Urls
    path('land/new/', LandCreate.as_view(), name='land_creat'),
    path('land/list/', LandListView.as_view(), name='land_list'),
    path('land/delete/<int:pk>/', LandDeleteView.as_view(), name='land_delete'),
    path('land/update/<int:pk>/', LandUpdateView.as_view(), name='land_update'),
    path('land/detail/<int:pk>/', LandDetailView.as_view(), name='land_detail'),
    path('home/', tableview, name='home'),
    path('', WelcomePage.as_view(), name='index.html')
]
