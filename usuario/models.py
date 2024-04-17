from django.db import models

class Usuario(models.Model):
    ALUNO = 'Aluno'
    PROFESSOR = 'Professor'
    CARGO_CHOICES = [
        (ALUNO, 'Aluno'),
        (PROFESSOR, 'Professor'),
    ]
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)
    cargo = models.CharField(max_length=9, choices=CARGO_CHOICES, default=ALUNO)

    def __str__(self) -> str:
        return self.nome