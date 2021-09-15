from collections import UserList
from flask import render_template,request, redirect, url_for
from ..requests import get_news, search_news, news_sources
from . import main


# Views



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Newsflash'
    current_news = get_news()

    newsSources = news_sources()

    search_topic = request.args.get('news_query')
    result_search_topic = search_news(search_topic)


    # if search_topic:
    #     return redirect(url_for('main.search'))
    # else:
    #     # return render_template('index.html', title = title, current_news =current_news)
    #     return redirect(url_for('main.routenews'))

    if search_topic:
        return render_template('search.html', news_choice=result_search_topic)
    else:
        return render_template('index.html', title = title, current_news =current_news, newsSources=newsSources)

@main.route('/home')
def routenews():
    title = 'Newsflash'
    current_news = get_news()
    return render_template('index.html', title = title, current_news =current_news)

@main.route('/search')
def search():
    search_topic = request.args.get('news_query')
    result_search_topic = search_news(search_topic)
    if search_topic:
        return render_template('search.html', news_choice=result_search_topic)
    else:
        return render_template('fourzerofour.html')


