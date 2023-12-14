FROM node:18-alpine

WORKDIR /usr/src/frontend

# Copy package.json and package-lock.json to the container
COPY package*.json /usr/src/frontend

# Install project dependencies
RUN npm install --legacy-peer-deps
RUN npm audit --force


# Copy the entire project to the container
COPY . /usr/src/frontend

# Start the development server with npm run dev
CMD [ "npm", "start"]