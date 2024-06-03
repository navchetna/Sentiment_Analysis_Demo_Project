FROM node:18-alpine

WORKDIR /app

RUN npm install prisma --save-dev

RUN npm init -y

CMD [ "npx", "prisma", "studio" ]
