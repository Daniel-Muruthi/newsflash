import urllib.request, json
from .models import news
from app import app

News = news.News


#Retrieving our API key
api_key = None
#Getting the news base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def process_news(news_list):
    """
    Function That processes the movie result and transforms them into a list of Objects
    """

    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(id, title, description, urlToImage, content)
            news_results.append(news_object)

    return news_results

def getNews():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=08db512f09b84c36a7d6f33d72d82fad'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news(news_results_list)

    return news_results

def search_news( ):
    search_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['sources']:
            search_news_list = search_news_response['sources']
            search_news_results = process_news(search_news_list)

    return search_news_results
