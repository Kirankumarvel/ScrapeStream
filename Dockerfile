FROM node:18-slim AS scraper-stage


# Install Chromium and Puppeteer dependencies
RUN apt-get update && apt-get install -y \
  chromium \
  fonts-liberation \
  --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install Node.js dependencies
COPY package.json ./
RUN npm install

# Copy the scraper script
COPY scrape.js ./

# Execute the scraping script to generate scraped_data.json
RUN node scrape.js

# Define environment variable
ENV SCRAPE_URL=https://example.com

# Run the scraper
CMD ["node", "scrape.js"]


FROM python:3.10-slim-buster AS server-stage

WORKDIR /app

# Copy the scraped data from the previous stage
COPY --from=scraper-stage /app/scraped_data.json ./

# Copy the server script
COPY server.py ./

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the server
CMD ["python", "server.py"]
