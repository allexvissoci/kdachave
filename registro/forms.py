from django import  forms
from .models import Registro

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro
		fields =[
					'dataEntrega',
					'dataPrevisaoRetorno',
					'dataRetorno',
					'pessoaEntregue',
					'pessoaRecebeu',
					'propriedade',
					'molhos',
				]