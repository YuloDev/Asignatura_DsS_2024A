import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Asignatura_DsS_2024A.settings')
django.setup()

from app.models import CustomUser, Categoria, Producto
import random

# Crear vendedores
vendedores = []
for i in range(5):  # Crear 5 vendedores
    vendedor = CustomUser.objects.create_user(
        username=f'vendedor{i + 1}',
        password='password123',
        is_seller=True,
        is_buyer=False
    )
    vendedores.append(vendedor)

# Crear categorías
categorias = []
nombres_categorias = ['Herramientas', 'Materiales de Construcción', 'Pinturas', 'Equipos de Protección', 'Accesorios']
for nombre in nombres_categorias:
    categoria = Categoria(nombre=nombre, record_ventas=random.randint(50, 200))
    categoria.save()
    categorias.append(categoria)

# Crear productos
nombres_productos = [
    'Martillo', 'Destornillador', 'Taladro', 'Sierra', 'Cemento', 'Arena', 'Ladrillos', 'Pintura Blanca',
    'Pintura Roja', 'Pintura Azul', 'Casco de Seguridad', 'Guantes de Trabajo', 'Botas de Seguridad',
    'Gafas de Protección', 'Mascarilla', 'Cinta Métrica', 'Llave Inglesa', 'Alicates', 'Cúter', 'Carretilla',
    'Nivel', 'Mezcladora', 'Tubería de PVC', 'Cable Eléctrico', 'Enchufes', 'Interruptores', 'Tornillos',
    'Clavos', 'Brocas', 'Limas'
]

for nombre in nombres_productos:
    producto = Producto(
        nombre=nombre,
        categoria=random.choice(categorias),
        vendedor=random.choice(vendedores),
        precio=round(random.uniform(5.0, 100.0), 2),
        costo=round(random.uniform(2.0, 50.0), 2),
    )
    producto.save()

print("Base de datos poblada con éxito")
