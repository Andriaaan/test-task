from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from .models import Brand
from .serializer import BrandSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timedelta
import jwt
from django.contrib.auth import authenticate

class GetBrandsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser', password='testpass')
        self.user = authenticate(username='testuser', email='testuser@testuser', password='testpass')
        self.token = RefreshToken(self.user)
        self.access_token = str(self.token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        Brand.objects.create(name='Brand 1', headquarters_country='Country 1')
        Brand.objects.create(name='Brand 2', headquarters_country='Country 2')
        Brand.objects.create(name='Brand 3', headquarters_country='Country 3')

    def test_get_all_brands(self):
        response = self.client.get(reverse('get_brands'))
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    