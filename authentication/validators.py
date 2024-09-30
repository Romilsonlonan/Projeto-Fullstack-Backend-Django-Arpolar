import re
from django.core.exceptions import ValidationError

def validar_cpf(value):
    # Verifica o formato do CPF com regex: xxx.xxx.xxx-xx
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError("CPF deve estar no formato xxx.xxx.xxx-xx")
