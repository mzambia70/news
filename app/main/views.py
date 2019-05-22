from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general_list = get_sources('general')
    business_list = get_sources('business')
    technoloogy_list = get_sources('technology')
    sports_list = get_sources('sports')
    health_list = get_sources('health')
    science_list = get_sources('science')
    entertainment_list = get_sources('entertainment')
    test_args = 'Working!'
    return render_template('index.html',
                            test_param=test_args,
                            general=general_list,
                            business=business_list,
                            technology=technoloogy_list,
                            sports=sports_list,
                            health=health_list,
                            science=science_list,
                            entertainment=entertainment_list)

@main.route('/news/<id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news_args = get_articles(id)
    highlight_args = 'Route Working!!'

    return render_template('news.html',highlight_param=highlight_args,news=news_args)