from django.db import models


from django.contrib.auth import get_user_model

User = get_user_model()


class Tutorial(models.Model):
    titulo = models.CharField(
      "Titulo",
      max_length=250,
    )
    codigo_video = models.TextField("Código de incorporação", null=True, blank=True)
    texto = models.TextField("Texto Principal")
    categoria = models.CharField(
        "Categoria",
        max_length=15,
        choices=[
            ("papelao", "Papelão"),
            ("vidro", "Vidro"),
            ("plastico", "Plástico"),
        ],
    )

