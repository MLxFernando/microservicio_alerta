# Usamos una imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos necesarios
COPY . /app/

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto donde correrá la app
EXPOSE 5000

# Comando para ejecutar el servidor
CMD ["python", "app.py"]
