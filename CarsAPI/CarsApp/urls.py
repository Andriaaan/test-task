from django.urls import path
from CarsApp import views

urlpatterns = [
    path('brands/', views.get_brands, name='get_brands'),
    path('models/', views.get_models),
    path('cars/', views.get_cars),
    path('cars/all/', views.get_all_cars),
    path('user/create/', views.UserRegistrationView),
    path('user/login/', views.UserLoginView),
]
