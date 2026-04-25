FROM node:20-slim

WORKDIR /app

# Copia apenas os arquivos de dependência primeiro
COPY package.json package-lock.json ./

# Ajusta configurações do npm para evitar timeout e reinstala dependências
RUN npm config set registry https://registry.npmjs.org/ \
    && npm config set fetch-retries 5 \
    && npm config set fetch-retry-mintimeout 20000 \
    && npm config set fetch-retry-maxtimeout 120000 \
    && npm install --legacy-peer-deps

# Copia o restante do código
COPY src ./src
COPY public ./public

EXPOSE 3000

CMD ["npm", "run", "dev"]
