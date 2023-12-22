# Azure Deployment Guide
This guide outlines the steps to create various resources in Azure using the Azure Portal.

# Project StreamPulse
For an application that utilizes Streamlit for real-time data visualization.

# Backend
The backend includes a Flask API responsible for connecting to an Azure MySQL database and exposing endpoints to retrieve degree and timestamp data.				 

# Structure
The backend directory contains:

app.py: Flask application file with API endpoints.
Dockerfile: Docker configuration for the backend service.

# Setup and Usage
Navigate to the backend directory.
Install dependencies and run the Flask API.

```bash
$ cd backend/
$ pip install -r requirements.txt
$ python app.py
```
Frontend
The frontend component is a Streamlit application designed to visualize data fetched from the Flask API.

# Structure
The frontend directory includes:

app.py: Streamlit application for data visualization.
Dockerfile: Docker configuration for the frontend service.

# Setup and Usage
Go to the frontend directory.
Install dependencies and run the Streamlit app.
```bash
$ cd frontend/
$ pip install -r requirements.txt
$ streamlit run app.py 
```

# Docker Compose
To run the entire project using Docker Compose:

Define backend and frontend services in a docker-compose.yml file.
Build and start the services with docker-compose up.
# Sample docker-compose.yml
```yaml
version: '3'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"  

  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
```
Replace ./backend and ./frontend with the actual paths to your backend and frontend directories.

# Contributing
Feel free to contribute by suggesting improvements, reporting issues, or adding new features through pull requests.
