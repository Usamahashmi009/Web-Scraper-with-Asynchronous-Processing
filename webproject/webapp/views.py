from django.shortcuts import render
from django.http import HttpResponse
from .tasks import scrape_website

def start_scraping(request):
    urls = [
        'https://www.geo.tv/',
        'https://www.bbc.com/'
    ]
    
    for url in urls:
        scrape_website.delay(url)
    
    return HttpResponse('Scraping started!')
