from django.shortcuts import render, redirect
from .models import Medicament, Vente
from .forms import MedicamentForm, VenteForm

# 1. Le Dashboard
def dashboard(request):
    medicaments = Medicament.objects.all()
    return render(request, 'dashboard.html', {'medicaments': medicaments}) # <-- Modifié ici

# 2. Ajouter un médicament
def ajouter_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MedicamentForm()
    return render(request, 'formulaire.html', {'form': form, 'titre': 'Ajouter un médicament'}) # <-- Modifié ici

# 3. Enregistrer une vente
def vendre_medicament(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            medicament = vente.medicament
            
            if medicament.quantite_stock >= vente.quantite_vendue:
                vente.save()
                medicament.quantite_stock -= vente.quantite_vendue
                medicament.save()
                return redirect('dashboard')
            else:
                form.add_error(None, f"Stock insuffisant ! Il ne reste que {medicament.quantite_stock} unités.")
    else:
        form = VenteForm()
    return render(request, 'formulaire.html', {'form': form, 'titre': 'Enregistrer une vente'}) # <-- Modifié ici