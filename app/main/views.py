from collections import UserList
from flask import render_template,request, redirect, url_for
from ..requests import get_news, search_news
from .import main

# Views



@main.route('/')
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
        # return render_template('index.html', title = title, current_news =current_news)
        return redirect(url_for('main.routenews'))

@main.route('/news')
def routenews():
    title = 'Home - Welcome to The best Movie Review Website Online'
    current_news = get_news()
    return render_template('index.html', title = title, current_news =current_news)



