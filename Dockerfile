# Usa la imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 8000

# Comando para correr la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
