from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15)
    status = models.CharField(
        max_length=100,
        choices=(
            ('A', 'Ativo'),
            ('I', 'Bloqueado'),
            ('C', 'Cancelado'),
        )
    )

    def --str - -(self):

    return self.none

class Curso(models.Model):
    curso = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    status = models.CharField(
        max_length=100,
        choices=(
            ('A', 'Ativo'),
            ('I', 'Inativo'),
        )
    )

    def --str - -(self):

    return self.none
