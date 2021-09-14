from flask import render_template,request, redirect, url_for
from app import app
from .requests import get_news, search_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    current_news = get_news()

    search_topic = request.args.get('news_query')
    result_search_topic = search_news(search_topic)

    if search_topic:
        return render_template('search.html', news_choice=result_search_topic)
    else:
        return render_template('index.html', title = title, current_news =current_news)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)