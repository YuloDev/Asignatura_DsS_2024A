from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from .models import Producto, Categoria
from django.contrib.auth import logout
from .forms import ProductoForm
from .decorators import seller_required  # Importa el decorador


def home(request):
    return render(request, 'home.html',
                  context={"productos": Producto.objects.all(), "categorias": Categoria.objects.all(),
                           "productos_destacados": []})


def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir según el tipo de usuario
                if user.is_seller:
                    return redirect('vendedor_home')
                else:
                    return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'inicio_sesion.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

@seller_required
def vendedor_home(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user  # Asocia el producto con el usuario autenticado
            producto.save()
            return redirect('vendedor_home')  # Redirige para evitar resubir el formulario
    else:
        form = ProductoForm()

    productos = Producto.objects.filter(vendedor=request.user)  # Opcional: mostrar productos del vendedor

    return render(request, 'vendedor_home.html', {
        'form': form,
        'productos': productos
    })


def cerrar_sesion(request):
    logout(request)
    return redirect('home')
