from django.db import models

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200) # Vai se tranformar em uma tabela dentro do Banco de Dados
    date_added = models.DateTimeField(auto_now_add=True) # Data que foi-se registrado/postado o texto

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text
    
class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # on_delete é obrigatório por conta da versão do Django
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries' # Para quando for feita várias entradas, para que não fique entrys, e sim o correto, entries

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...' # Limita para os primeiros 50 caractéres
