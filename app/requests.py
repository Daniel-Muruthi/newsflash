import urllib.request, json
from .models import News_Source, News_Article

#Retrieving our API key
api_key = None
#Getting the news base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']