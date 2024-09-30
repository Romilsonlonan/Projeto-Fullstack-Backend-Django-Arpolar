from django.urls import path
from .viewsets import ColaboradorViewSet 
from authentication.api.viewsets import LoginAPIView


urlpatterns = [
    path('colaboradores/', ColaboradorViewSet.as_view({'get': 'list', 'post': 'create'}), name='colaborador-list'),
    # Se você precisar de outras operações, adicione-as aqui
    path('colaboradores/<int:pk>/', ColaboradorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='colaborador-detail'),
    path('login/', LoginAPIView.as_view(), name='login'),

]

