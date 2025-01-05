from django.urls import path
from django.contrib import admin
from .api import *
from . import views
from . import api
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TechNest, name="techNest"),
    path('gearGallery/', views.GearGallery, name="gearGallery"),
    path('login/', views.Login, name="login"),
    path('signup/', views.Signup, name="signup"),
    path('logout/', views.Logout, name='logout'),
    path('pcAssembly/', views.PCAssembly, name="pcAssembly"),
    path('parts/', views.Parts, name="parts"),
    path('part/<str:part_category>/<int:part_id>', views.Part_Det, name='partDet'),
    path('saved-customizations/', TemplateView.as_view(template_name='Customization_View.html'), name='savedCustomizations'),
    path('main/', views.Main, name='main'),

    # API Endpoints
    path('api/pc_assembly/', api.PCAssemblyAPI.as_view(), name='pcAssemblyAPI'),
    path('api/save-customizations/', SaveCustomizations.as_view(), name='saveCustomizations'),
    path('api/delete-customization/<int:saved_id>', DeleteCustomizations.as_view(), name='delete-customization'),
] 