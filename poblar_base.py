import os
import django
import random
from django.core.exceptions import ObjectDoesNotExist

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Asignatura_DsS_2024A.settings')
django.setup()

from app.models import CustomUser, Categoria, Producto


def create_or_get_vendedores():
    vendedores = []
    for i in range(5):  # Crear 5 vendedores
        vendedor, created = CustomUser.objects.get_or_create(
            username=f'vendedor{i + 1}',
            defaults={
                'password': 'password123',
                'is_seller': True,
                'is_buyer': False
            }
        )
        if created:
            vendedor.set_password('password123')
            vendedor.save()
        vendedores.append(vendedor)
    return vendedores


def create_or_get_categorias():
    categorias = []
    nombres_categorias = ['Herramientas', 'Materiales de Construcción', 'Pinturas', 'Equipos de Protección',
                          'Accesorios']
    for nombre in nombres_categorias:
        categoria, created = Categoria.objects.get_or_create(
            nombre=nombre,
            defaults={'record_ventas': random.randint(50, 200)}
        )
        if created:
            categoria.save()
        categorias.append(categoria)
    return categorias


def create_or_get_productos(vendedores, categorias):
    nombres_productos = [
        'Martillo', 'Destornillador', 'Taladro', 'Sierra', 'Cemento', 'Arena', 'Ladrillos', 'Pintura Blanca',
        'Pintura Roja', 'Pintura Azul', 'Casco de Seguridad', 'Guantes de Trabajo', 'Botas de Seguridad',
        'Gafas de Protección', 'Mascarilla', 'Cinta Métrica', 'Llave Inglesa', 'Alicates', 'Cúter', 'Carretilla',
        'Nivel', 'Mezcladora', 'Tubería de PVC', 'Cable Eléctrico', 'Enchufes', 'Interruptores', 'Tornillos',
        'Clavos', 'Brocas', 'Limas'
    ]

    for nombre in nombres_productos:
        producto, created = Producto.objects.get_or_create(
            nombre=nombre,
            defaults={
                'categoria': random.choice(categorias),
                'vendedor': random.choice(vendedores),
                'precio': round(random.uniform(5.0, 100.0), 2),
                'costo': round(random.uniform(2.0, 50.0), 2),
            }
        )
        if created:
            producto.save()


def main():
    try:
        vendedores = create_or_get_vendedores()
        categorias = create_or_get_categorias()
        create_or_get_productos(vendedores, categorias)
        print("Base de datos poblada con éxito")
    except Exception as e:
        print(f"Error al poblar la base de datos: {e}")


if __name__ == "__main__":
    main()
