from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
import os



NEW_SAVE_DIR = 'E:\MM\WebScrapy celery'
os.makedirs(NEW_SAVE_DIR, exist_ok=True)


@shared_task(bind=True, max_retries=3)
def scrape_website(self, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract and save title and content
        title = soup.title.string if soup.title else 'No Title'
        content = soup.get_text()

         # Create a safe file name
        file_name = url.split('//')[-1].replace('/', '_') + '.txt'
        file_path = os.path.join(NEW_SAVE_DIR, file_name)  # Use new path

        # Save data to a file
        with open(file_path, 'w') as file:
            file.write(f"Title: {title}\n\nContent:\n{content}")
        print(f"File created: {file_path}")

    except requests.exceptions.RequestException as exc:
        # Retry the task if an exception occurs
        raise self.retry(exc=exc)

