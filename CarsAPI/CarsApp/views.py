from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Brand, Model, Car
from .serializer import BrandSerializer, ModelSerializer, CarSerializer, UserSerializer
from django.http.response import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


@api_view(['POST'])
def UserRegistrationView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def UserLoginView(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=username, email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_brands(request):
    name = request.GET.get('name')
    country = request.GET.get('country')
    if name:
        queryset = Brand.objects.filter(name=name)
    elif country:
        queryset = Brand.objects.filter(headquarters_country=country)
    else:
        queryset = Brand.objects.all()
    serializer = BrandSerializer(queryset, many=True)
    return Response(serializer.data,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_models(request):
    queryset = Model.objects.all()
    serializer = ModelSerializer(queryset, many=True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cars(request):
    queryset = Car.objects.filter(is_on_sale=True)
    
    brand_name = request.GET.get('brand_name')
    if brand_name:
        queryset = queryset.filter(brand__name__icontains=brand_name)

    model_name = request.GET.get('model_name')
    if model_name:
        queryset = queryset.filter(model__name__icontains=model_name)

    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min and price_max:
        queryset = queryset.filter(price__gte=price_min, price__lte=price_max)

    mileage_min = request.GET.get('mileage_min')
    mileage_max = request.GET.get('mileage_max')
    if mileage_min and mileage_max:
        queryset = queryset.filter(mileage__gte=mileage_min, mileage__lte=mileage_max)

    exterior_color = request.GET.get('exterior_color')
    if exterior_color:
        queryset = queryset.filter(exterior_color=exterior_color)

    interior_color = request.GET.get('interior_color')
    if interior_color:
        queryset = queryset.filter(interior_color=interior_color)

    fuel_type = request.GET.get('fuel_type')
    if fuel_type:
        queryset = queryset.filter(fuel_type=fuel_type)

    transmission = request.GET.get('transmission')
    if transmission:
        queryset = queryset.filter(transmission=transmission)

    engine = request.GET.get('engine')
    if engine:
        queryset = queryset.filter(engine=engine)

    year_min  = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    if year_min and year_max:
        queryset = queryset.filter(
            Q(model__year_of_issue__gte=year_min) & Q(model__year_of_issue__lte=year_max))

    body_style = request.GET.get('body_style')
    if body_style:
        queryset = queryset.filter(body_style=body_style)

    serializer = CarSerializer(queryset, many=True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_cars(request):
    queryset = Car.objects.all()

    brand_name = request.GET.get('brand_name')
    if brand_name:
        queryset = queryset.filter(brand__name__icontains=brand_name)

    model_name = request.GET.get('model_name')
    if model_name:
        queryset = queryset.filter(model__name__icontains=model_name)

    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min and price_max:
        queryset = queryset.filter(price__gte=price_min, price__lte=price_max)

    mileage_min = request.GET.get('mileage_min')
    mileage_max = request.GET.get('mileage_max')
    if mileage_min and mileage_max:
        queryset = queryset.filter(mileage__gte=mileage_min, mileage__lte=mileage_max)

    exterior_color = request.GET.get('exterior_color')
    if exterior_color:
        queryset = queryset.filter(exterior_color=exterior_color)

    interior_color = request.GET.get('interior_color')
    if interior_color:
        queryset = queryset.filter(interior_color=interior_color)

    fuel_type = request.GET.get('fuel_type')
    if fuel_type:
        queryset = queryset.filter(fuel_type=fuel_type)

    transmission = request.GET.get('transmission')
    if transmission:
        queryset = queryset.filter(transmission=transmission)

    engine = request.GET.get('engine')
    if engine:
        queryset = queryset.filter(engine=engine)

    year_min  = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    if year_min and year_max:
        queryset = queryset.filter(
            Q(model__year_of_issue__gte=year_min) & Q(model__year_of_issue__lte=year_max))

    body_style = request.GET.get('body_style')
    if body_style:
        queryset = queryset.filter(body_style=body_style)

    serializer = CarSerializer(queryset, many=True)
    return JsonResponse(serializer.data,safe=False)

