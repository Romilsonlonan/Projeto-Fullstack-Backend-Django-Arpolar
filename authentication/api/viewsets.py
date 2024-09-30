import random
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from authentication.models import Colaborador
from authentication.api.serializers import LoginSerializer, ColaboradorSerializer


class ColaboradorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            add_matricula = serializer.validated_data.get('add_matricula')
            senha = serializer.validated_data.get('senha')
            
            # Tentar buscar o colaborador usando a matrícula
            colaborador = get_object_or_404(Colaborador, add_matricula=add_matricula)
            
            # Verificar se a senha está correta
            if colaborador.senha == senha:
                # Gerar o token JWT usando o colaborador autenticado
                refresh = RefreshToken.for_user(colaborador)

                return Response({
                    "success": True,
                    "message": "Login bem-sucedido",
                    "colaborador": colaborador.nome,
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Senha incorreta"
                }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

