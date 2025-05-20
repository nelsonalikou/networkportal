# Étape 1 : build de la Vue app
FROM node:18-alpine as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Étape 2 : serveur Nginx pour servir la build
FROM nginx:stable-alpine

# Copier la build Vue dans le dossier Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copier la config Nginx custom
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
