
# ScrapeStream 🕸️📦💻 — Web Scraping, Data Storage, and Server


A simple Flask-based server to serve scraped data and provide basic endpoints for monitoring and data retrieval. This project uses a multi-stage Docker build to keep the final image size minimal and organized.
ScrapeStream is a robust multi-stage data scraping and server application built using Flask and Puppeteer. It enables data extraction and serves the data through a simple API endpoint.

## 📦 Features

- Serves scraped data in JSON format
- Provides a home route for basic monitoring
- Multi-stage Docker build for optimized image size
- Error handling for missing data files

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed on your system:

- Docker
- Node.js
- Python 3

---

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd multi-stage-scraper-server
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:

   ```bash
   npm install
   ```

---

### Build Docker Image

Build the Docker image using the following command:

```bash
docker build -t scraper-server .
```

---

### Run Docker Container

Run the Docker container using:

```bash
docker run -p 5000:5000 scraper-server
```

Access the server at: [http://localhost:5000](http://localhost:5000)

---

## Accessing Endpoints

- `/` - Home route
- `/data` - Retrieve scraped data in JSON format

---

## 📂 Copy Data to Container

If you need to copy the `scraped_data.json` file to the container:

```bash
docker cp scraped_data.json <container_id>:/app/
```

---

## 📋 Checking Running Containers

To view running containers:

```bash
docker ps
```

---

## 📖 Checking Logs

To view the logs of a running container:

```bash
docker logs <container_id>
```

---

## ✅ Troubleshooting and Common Issues

### Port Already in Use

**Error:**

```
Bind for 0.0.0.0:5000 failed: port is already allocated
```

**Solution:** Stop the running container or use a different port:

```bash
docker run -p 8080:5000 scraper-server
```

---

### Module Not Found Error (e.g., Puppeteer)

Run the following command in the project directory to resolve missing Node.js dependencies:

```bash
npm install
```

---

### Data File Not Found Error

Ensure that `scraped_data.json` exists in the container by running:

```bash
docker exec -it <container_id> ls /app/
```

---

### Container Not Running

**Error:**

```
Error response from daemon: container <id> is not running
```

**Solution:** Ensure that the container is started:

```bash
docker start <container_id>
```

---

### Unable to Access Internal IP (e.g., 172.17.0.2:5000)

Access the application using:

- [http://localhost:5000](http://localhost:5000)
- [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

---

## 🌐 Learn More

Check out the detailed blog post about ScrapeStream and its implementation:  
[ScrapeStream: Multi-Stage Web Scraping Server](https://kirankumarvel.wordpress.com/2025/05/13/scrapestream-multi-stage-web-scraping-server/)

---

## 📜 License

This project is licensed under the MIT License.

