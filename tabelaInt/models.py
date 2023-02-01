from django.conf import settings
from django.db import models


class TabelaInt(models.Model):
    codigo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=255)
    tabela = models.CharField(
        default="000",
        max_length=3,
        choices=(
            ('000', 'Selecionar...'),
            ('001', 'Tabela Estado'),
            ('002', 'Tabela Cor'),
            ('003', 'Tabela Tamanho'),
            ('100', 'Tabela Categoria'),
        )
    )

    def __str__(self):
        return f'TabelaInt {self.pk}, {self.tabela}, {self.codigo}'
