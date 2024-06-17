FROM node:18

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 13002

CMD [ "npm", "run", "dev" ]