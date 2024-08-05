import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm, ProductoForm
from .models import Producto, Categoria
from .decorators import seller_required  # decorador de seguridad

logger = logging.getLogger(__name__)

def home(request):
    logger.debug('Página de inicio cargada.')
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
                logger.info(f'Inicio de sesión exitoso para el usuario: {username}')
                # Redirigir según el tipo de usuario
                if user.is_seller:
                    return redirect('vendedor_home')
                else:
                    return redirect('home')
            else:
                logger.error(f'Inicio de sesión fallido para el usuario: {username}')
        else:
            logger.warning('Formulario de inicio de sesión no válido.')
    else:
        form = LoginForm()
    return render(request, 'inicio_sesion.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f'Nuevo usuario registrado: {user.username}')
            return redirect('inicio_sesion')  # Asumiendo que el nombre de la URL es 'inicio_sesion'
        else:
            logger.warning('Formulario de registro no válido.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

@seller_required
def vendedor_home(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user  # Asociar el producto con el usuario autenticado
            producto.save()
            logger.info(f'Nuevo producto agregado por el vendedor: {request.user.username}')
            return redirect('vendedor_home')  # Redirigir para evitar resubir el formulario
        else:
            logger.warning('Formulario de producto no válido.')
    else:
        form = ProductoForm()

    productos = Producto.objects.filter(vendedor=request.user)
    logger.debug(f'Productos cargados para el vendedor: {request.user.username}')

    return render(request, 'vendedor_home.html', {
        'form': form,
        'productos': productos
    })

def cerrar_sesion(request):
    logger.info(f'Usuario {request.user.username} cerró sesión.')
    logout(request)
    return redirect('home')
