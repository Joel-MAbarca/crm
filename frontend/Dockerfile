FROM node:18-alpine

ARG VITE_API_URL

WORKDIR /app/frontend

COPY frontend/package*.json ./
COPY frontend/.env.production.local .

RUN npm install

COPY frontend/ .

RUN VITE_API_URL=$VITE_API_URL npm run build

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "${PORT:-3000}"]