FROM node:20-slim

WORKDIR /app

# Copiamos los archivos de dependencias primero para aprovechar la caché de Docker
COPY package*.json ./
RUN npm install

# Copiamos el resto del código
COPY . .

EXPOSE 5173

# Comando para arrancar Vite con soporte para red externa (host 0.0.0.0)
CMD ["npm", "run", "dev", "--", "--host"]