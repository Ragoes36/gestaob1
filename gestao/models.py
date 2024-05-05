from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Segmento(models.Model):
    id = models.AutoField(primary_key=True)
    opcoes = models.CharField(max_length=200)

    
    def __str__(self):
        return self.opcoes

    class Meta:
        ordering = ['opcoes']
        

class Empresas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    segmento = models.ForeignKey(Segmento, on_delete=models.PROTECT, related_name='nome_segmento')
    contatos = models.CharField(max_length=25, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    descrição = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class AvaliacaoPrestadorServico(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    classificacao = models.DecimalField(
        max_digits=1,
        decimal_places=0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Avaliação de {self.empresa.nome}"




class Sugestoes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    condominio = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    unidade = models.CharField(max_length=20)
    incoveniente = models.TextField(max_length=500)
    sugestao_de_melhoria = models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['condominio']
    

class Reclamacoes(models.Model):
    id = models.AutoField(primary_key=True)
    reclamante = models.CharField(max_length=200)
    condominio = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    unidade = models.CharField(max_length=20)
    reclamado = models.CharField(max_length=200)
    ocorrencia = models.TextField(max_length=3000)


    def __str__(self):
        return self.reclamante
    
    class Meta:
        ordering = ['condominio']
    