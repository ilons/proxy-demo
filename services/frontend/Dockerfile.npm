FROM node:13.12.0-alpine

RUN npm install -g create-react-app@3.4.1

WORKDIR /
RUN npm init react-app app --use-npm
WORKDIR /app

ENV PATH=/app/node_modules/.bin:$PATH

COPY package.json .
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY src/ src/

CMD ["npm", "start"]
