from django.contrib import admin

from eventos.models import Categoria , Evento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao']
    search_fields = [ 'nome','descricao']
 

 
@admin.action(description='Marcar como publicado')   
def marcar_publicado(modeladmin , request , queryset):
    queryset.update(publicado = True)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome','categoria','data','publicado']
    search_fields = ['nome','descricao','categoria__nome']
    list_filter = ['publicado','data','categoria']
    actions = [marcar_publicado]
     