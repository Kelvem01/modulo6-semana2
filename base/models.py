from django.db import models

class Contato(models.Model):
    
    PREFERENCIA_EVENTO_OPCOES =(
        ('todos','Todos'),
        ('musicais','Eventos Musicais'),
        ('esportivos','Eventos Esportivos'),
        ('educativos','Eventos Educativos'),
        
    )
    
    nome = models.CharField(verbose_name='Nome',max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    preferencia_evento = models.CharField(
        verbose_name='Preferência de Evento', max_length=20, default='todos',
        choices=PREFERENCIA_EVENTO_OPCOES
    )
    observacao = models.TextField(verbose_name='Observação',blank= True)
    enviado_em = models.DateTimeField(verbose_name='Enviado em', auto_now_add= True)
    modificado_em = models.DateTimeField(verbose_name='Modificado em', auto_now= True)
    
