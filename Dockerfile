# Usa una imagen base de Ubuntu
FROM ubuntu:20.04

# Define el autor de la imagen
LABEL maintainer="tu_email@dominio.com"

# Actualiza el sistema e instala algunos paquetes
RUN apt-get update && apt-get install -y \
    curl \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia archivos locales al contenedor
COPY . /app

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 8080

# Define el comando por defecto para ejecutar cuando se arranca el contenedor
CMD ["bash"]
