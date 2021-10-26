from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    procedimento = models.CharField(max_length=100, verbose_name='procedimento')
    tipo = models.CharField(max_length=100, verbose_name='tipo')
    investigado = models.CharField(max_length=100, verbose_name='investigado')
    vitima = models.CharField(max_length=100, verbose_name='vitima')
    fato = models.CharField(max_length=100, verbose_name='fato')
    autos = models.CharField(max_length=100, verbose_name='autos', blank=True, null=True)
    data_remessa = models.DateField(verbose_name='Data da Remessa',  null=True, blank=True)
    data_instauracao = models.DateField(verbose_name='Data da Instauração', default=None)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.procedimento

    def get_data_instauracao(self):
        return self.data_instauracao.strftime('%d/%m/%Y')

    def get_data_input_instauracao(self):
        return self.data_instauracao.strftime('%Y-%m-%d')

    def get_data_remessa(self):
        return self.data_remessa.strftime('%d/%m/%Y')

    def get_data_input_remessa(self):
        return self.data_remessa.strftime('%Y-%m-%d')