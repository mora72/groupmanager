from django.db import models


class Uf(models.Model):
    uf = models.CharField(max_length=2)
    nomeuf = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'UFs'

    def __str__(self):
        return self.nomeuf


class Grupo(models.Model):
    opcoesstatus = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=opcoesstatus, default='A')
    cidade = models.CharField(max_length=50)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    dataini = models.DateField(null=True, blank=True)
    nomecontato = models.CharField(max_length=50, null=True, blank=True)
    telefonecontato = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.nome


class Integrante(models.Model):
    opcoesgenero = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    opcoesstatus = (
        ('ATV', 'Ativo'),
        ('AUS', 'Ausente'),
        ('DIS', 'Disciplina'),
        ('VIS', 'Visitante'),
        ('INT', 'Interessado')
    )
    opcoes_estado_civil = (
        ('CAS', 'Casado'),
        ('SOL', 'Solteiro'),
        ('DIV', 'Divorciado'),
        ('SEP', 'Separado'),
        ('VIU', 'Viúvo')
    )
    nome = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1, choices=opcoesgenero)
    datanasc = models.DateField(null=True, blank=True)
    estadocivil = models.CharField(max_length=20, choices=opcoes_estado_civil, null=True, blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    status = models.CharField(max_length=3, choices=opcoesstatus)
    observacoes = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Integrantes'

    def __str__(self):
        return self.nome


class Distancia(models.Model):
    origem = models.CharField(max_length=50)
    cidade_destino = models.CharField(max_length=50)
    uf_destino = models.ForeignKey(Uf, on_delete=models.CASCADE)
    distancia = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Distâncias'

    def __str__(self):
        nome = f'{self.origem} / {self.cidade_destino} - {self.uf_destino}'
        return nome
