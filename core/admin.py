from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','procedimento','fato','investigado','data_instauracao')

admin.site.register(Evento,EventoAdmin)