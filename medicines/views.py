from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Medicine
from .forms import MedicineForm

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines/medicine_list.html', {'medicines': medicines})

def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'GET':
        return JsonResponse({
            'name': medicine.name,
            'generic_name': medicine.generic_name,
            'manufacturer': medicine.manufacturer,
            'description': medicine.description,
            'price': medicine.price,
            'batch_number': medicine.batch_number,
            'other_details': medicine.other_details,
        })

@login_required
def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicines/medicine_form.html', {'form': form})

@login_required
def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'medicines/medicine_form.html', {'form': form})

@login_required
def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'medicines/medicine_confirm_delete.html', {'medicine': medicine})
