from django.shortcuts import render
from django.utils import timezone
from .models import Denunc
from django.shortcuts import render, get_object_or_404
from .forms import DenuncForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



def denunc_list(request):
    denuncs = Denunc.objects.all()
    return render(request, 'blog/denunc_list.html', {'denuncs': denuncs})

def denunc_detail(request, pk):
    denunc = get_object_or_404(Denunc, pk=pk)
    return render(request, 'blog/denunc_detail.html', {'denunc': denunc})

@login_required
def denunc_new(request):
    if request.method == "POST":
        form = DenuncForm(request.POST)
        if form.is_valid():
            denunc = form.save(commit=False)
            denunc.author = request.user
            denunc.published_date = timezone.now()
            denunc.save()
            return redirect('denunc_detail', pk=denunc.pk)
    else:
        form = DenuncForm()
    return render(request, 'blog/denunc_edit.html', {'form': form})

@login_required
def denunc_edit(request, pk):
    denunc = get_object_or_404(Denunc, pk=pk)
    if request.method == "POST":
        form = DenuncForm(request.POST, instance=denunc)
        if form.is_valid():
            denunc = form.save(commit=False)
            denunc.author = request.user
            denunc.published_date = timezone.now()
            denunc.save()
            return redirect('denunc_detail', pk=denunc.pk)
    else:
        form = DenuncForm(instance=denunc)
    return render(request, 'blog/denunc_edit.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = UserCreationForm()
    return render(request, 'registration/register.html', {'register_form': register_form})


def profil(request):
    return render(request, 'blog/profil.html')



