from django.db import models

class Categoria(models.Model):
    nome = models.CharField('Nome',max_length=50)
    descricao = models.TextField('Descrição',blank=True)
    
    def __str__(self) :
        return self.nome
    
    class Meta :
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
        
class Evento(models.Model):
    
    nome = models.CharField('Nome',max_length=50)
    categoria = models.ForeignKey(Categoria ,models.CASCADE)
    descricao = models.TextField('Descrição',blank=True)
    data = models.DateField('Data do Evento',null=True,blank=True)
    criado_em = models.DateTimeField('Criado em ',auto_now_add=True)
    criado_por = models.ForeignKey('auth.User', models.SET_NULL, null=True, blank=True)
    
    def __str__(self) :
        return self.nome
    
    class Meta :
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'


class InscricaoEvento(models.Model):
    nome = models.CharField ('Nome',max_length=100)
    email = models.EmailField('E-mail')
    evento = models.ForeignKey(Evento, models.CASCADE)
    confirmado = models.BooleanField('Confirmado', default=False)
    criado_em = models.DateTimeField('Criado em', auto_now_add= True)
    
    def __str__(self):
        return f'[{self.evento}]{self.nome}'