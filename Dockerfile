# Base image
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Build the app
RUN npm run build

# Expose the app's port
EXPOSE 3000

# Start the app
CMD [ "npm", "run", "dev", "--port", "3000" ]