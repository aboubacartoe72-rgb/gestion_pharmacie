from django.db import models

class Medicament(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} (Stock: {self.quantite_stock})"

class Vente(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite_vendue = models.IntegerField()
    date_vente = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vente de {self.quantite_vendue} {self.medicament.nom}"