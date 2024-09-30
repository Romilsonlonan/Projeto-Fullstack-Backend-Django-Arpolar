from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers  # Adicione esta linha
from authentication.api.viewsets import ColaboradorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 


route = routers.DefaultRouter()
route.register(r'senha', ColaboradorViewSet, basename='Colaborador')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),    
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('api/', include('authentication.api.urls')),  # Incluindo as URLs da API
    #path('api/login/', LoginAPIView.as_view(), name='login'), 
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/', include('authentication.urls')),  # Incluindo as URLs do app authentication

]
