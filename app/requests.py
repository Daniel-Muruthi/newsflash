from app import app
from app.models.news import News
import urllib.request, json

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=08db512f09b84c36a7d6f33d72d82fad'.format()

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        get_news_results = None

        if get_news_response['sources']:
            get_news_results_list = get_news_response['sources']
            get_news_results = process_results(get_news_results_list)


    return get_news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        if id:
            news_object = News(id,name,description,url,category,country)
            news_results.append(news_object)

    return news_results