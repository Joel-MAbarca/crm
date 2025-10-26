# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app/frontend

COPY package*.json /app/frontend/
RUN npm install

COPY . /app/frontend/

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "3000"]