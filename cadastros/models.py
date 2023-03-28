from django.db import models

# Create your models here.

class Fazenda(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Usuário")
    telephone = models.CharField(max_length=15, black=True, null=True)
    cpf_cnpj = models.CharField(max_length=18, help_text="Preencha com CPF ou CNPJ ")
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.nome} ({self.cpf_cnpj})"

        
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=18)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.PROTECT
    )


    def __str__(self):
        return f"{self.nome} ({self.login})"

class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    permicao = models.ForeignKey(
        Permicao, on_delete=models.PROTECT
    )

class Historico(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.PROTECT
    )

