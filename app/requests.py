from app.models.news import News, NewsSources, SearchNewsAll
import urllib.request, json

# Getting api key
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'http://newsapi.org/v2/everything?q=all&sortBy=popularity&pageSize=10&page=1&apiKey=08db512f09b84c36a7d6f33d72d82fad'.format()

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        get_news_results = None

        if get_news_response['articles']:
            get_news_results_list = get_news_response['articles']
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
        title = news_item.get('title')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')

        if id:
            news_object = News(title,name,description,url,urlToImage,content,author,publishedAt)
            news_results.append(news_object)

    return news_results

def process_every_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')

        if id:
            news_object = SearchNewsAll(title,name,description,url,urlToImage,content,author,publishedAt)
            news_results.append(news_object)

    return news_results


def search_news(topic):
    get_news_details_url = 'http://newsapi.org/v2/everything?q={}&apiKey=08db512f09b84c36a7d6f33d72d82fad'.format(topic)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        get_news_results = None


        if news_details_response['articles']:
            get_news_results_list = news_details_response['articles']
            get_news_results = process_every_results(get_news_results_list)

    return get_news_results

def process_sources_results(news_list):

    news_results=[]
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        if id:
            news_object = NewsSources(id,name,description,url)
            news_results.append(news_object)

    return news_results

def news_sources():
    get_news_sources_url ='https://newsapi.org/v2/top-headlines/sources?apiKey=08db512f09b84c36a7d6f33d72d82fad'.format()

    with urllib.request.urlopen(get_news_sources_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        get_news_results = None

        if news_details_response['sources']:
            get_news_results_list = news_details_response['sources']
            get_news_results = process_sources_results(get_news_results_list)

    return get_news_results
