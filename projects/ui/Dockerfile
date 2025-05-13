FROM node:22-alpine
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# In real life a dedicated http server would be better like NGINX or Caddy
EXPOSE 4173
CMD ["npm","run","preview","--","--host","0.0.0.0","--port","4173"]
