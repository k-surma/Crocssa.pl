FROM node:20-alpine

WORKDIR /app

# kopiujemy wyłącznie package.json
COPY package.json ./
RUN npm install

# reszta kodu
COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
