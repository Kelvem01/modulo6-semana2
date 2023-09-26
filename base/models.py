from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome',max_length=50)
    email = models.EmailField('E-mail',)
    preferencia_evento = models.CharField('Preferencia Eventos',max_length=30 ,blank= True)
    observacao = models.TextField('Observação',blank=True)