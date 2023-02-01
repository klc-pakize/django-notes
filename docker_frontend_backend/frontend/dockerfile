FROM node:19-slim
WORKDIR /frontend
COPY package.json .
RUN npm install
COPY . . 
CMD ["npm", "start"]
EXPOSE 3000

