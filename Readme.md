
# Web Scraper with Asynchronous Processing

This project demonstrates a web scraping application built using Django, Celery, and BeautifulSoup. It performs web scraping tasks asynchronously with Celery and saves the extracted data to files.

## Project Overview

- **Django**: Framework for building the web application.
- **Celery**: Asynchronous task queue to handle web scraping tasks.
- **BeautifulSoup**: Library for parsing HTML and extracting data.
- **Requests**: Library for making HTTP requests.

## Features

- Asynchronous web scraping using Celery.
- Extracts and saves webpage titles and content to text files.
- Handles retries for failed scraping tasks.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Usamahashmi009/Web-Scraper-with-Asynchronous-Processing.git
   cd Web-Scraper-with-Asynchronous-Processing
