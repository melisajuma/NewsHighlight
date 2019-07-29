from flask import render_template,request,redirect,url_for  
from ..request import get_news_sources,get_news_source
from ..models import Source,Article
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting news sources based on the category from the news sources endpoint
    general = get_news_sources('general')
    business = get_news_sources('business')
    technology = get_news_sources('technology')
    health = get_news_sources('health')
    science = get_news_sources('science')
    sports = get_news_sources('sports')
    
    title = 'The best news Highlits In The World'
    
    search_news_source = request.args.get('news_query')

    if search_news_source:
        return redirect(url_for('main.index',news_name = search_news_source))
    else:
        return render_template('index.html',title = title,general = general ,business = business, technology = technology,health=health,science=science,sports=sports)

@main.route('/source/<id>')
def source(id):
    '''
    View root page function theat returns the index pages and its  data 
    '''
    source = get_news_source(id)
    newsid = id.capitalize()
    title = f'{newsid}'
    details = id.capitalize()
    content = f'{details}'
    # articles = news_source.get_news_source(source.id)
    return render_template('news_source.html',  title = title, id = newsid ,source = source ,content = content)