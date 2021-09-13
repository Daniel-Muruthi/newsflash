from flask import render_template, request, redirect,url_for
from app import app
from .requests import getNews


#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting popular movies

    # bbc_news = getNews('bbc-news')

    webtitle="NewsFlash"

    generalNews = getNews()


    return render_template('index.html', title = webtitle, generalNews = generalNews)

@app.route('/news/<news_id>')
def newsstory(news_id):
    '''
    View newsflash page that returns news details page and its data
    '''

    return render_template('news.html', id = news_id)
