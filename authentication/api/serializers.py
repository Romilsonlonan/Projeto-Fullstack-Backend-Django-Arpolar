from rest_framework import serializers
from authentication import models 


class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Colaborador
        fields = '__all__'
        
class LoginSerializer(serializers.Serializer):
    add_matricula = serializers.CharField(max_length=5)
    senha = serializers.CharField(max_length=6)
    
    def validate_login(self, add_matricula, senha):
        """
        Método para validar a matrícula e a senha do colaborador.
        """
        try:
            colaborador = models.Colaborador.objects.get(add_matricula=add_matricula)
            if colaborador.senha == senha:
                return colaborador
            else:
                raise serializers.ValidationError("Senha inválida.")
        except models.Colaborador.DoesNotExist:
            raise serializers.ValidationError("Colaborador não encontrado.")