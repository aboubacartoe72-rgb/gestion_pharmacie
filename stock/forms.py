from django import forms
from .models import Medicament, Vente

class MedicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = ['nom', 'description', 'prix', 'quantite_stock']

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['medicament', 'quantite_vendue']