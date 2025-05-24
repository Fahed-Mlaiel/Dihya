# Dihya Logos – Exemples Docker/K8s

## Dockerfile pour serveur logos Node.js
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY . .
RUN npm install --production
EXPOSE 4001
CMD ["node", "serve_logos.js"]
```

## Docker Compose
```yaml
services:
  logos:
    build: .
    ports:
      - "4001:4001"
    volumes:
      - ./Dihya/assets/logos:/app
```
