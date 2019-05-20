import urllib.request
import json  # help connection to the api and send request
from .models import news  # importin news classfrom the models

News - news.News

#Getting api key
api_key = None

#Getting the news base url
base_url = None


news_url = None

#taking the app instances and replace values of none variable app confiduration objects


def configure_request(app):
    global api_key, base_url, news_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    news_url = app.config['NEWS_BASE_URL']


def search_news(movie_name):
    search_news_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(
        api_key, news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

    if search_news_response['results']:
        search_news_list = search_news_response['results']
        search_news_results = process_results(search_news_list)

    return search_news_results


def get_sources(category):  # fn that takes catagory as argument
  '''
  Function that gets the json response to our url request
  '''
  get_sources_url = base_url.format(category, api_key)

  # with being the context manager to request
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    # changin the json to a dictionary in python
    sources_results = None

    if get_sources_response['results']:
      sources_results_list = get_sources_response['results']
      sources_results = process_results(sources_results_list)
  return sources_results


def process_sources(sources_list):
  '''
  Function that processor the news result and transform them to a list of objects
  Args:
       news_list: A list of dictionaries that contain news details
  Returns :
      news_results: A list of news objects
  '''
  sources_results = []
  for sources_item in news_list:
    id = sources_item.get('id')
    name = sources_item.get('name')
    description = sources_item.get('description')
    url = sources_item.get('url')
    category = sources_item.get('category')
    language = sources_item.get('language')
    country = sources_item.get('country')
    if poster:
      sources_object = News(id, name, descrition, url,
                            category, language, country)
      sources_results.append(sources_object)

def get_news(id):
    get_news_url = news_url.format(id, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        # news_details_data = url.read()
        # news_details_response = json.loads(news_details_data)
        news_results = json, loads(url.read())

    news_object = None
    if news_results['news']:
        news_object - process_news(news_results['news'])

    return news_object
def process_news(news_list):
    '''
    '''
    news_object = []
    for news_item in news_list:
        id = news _item.get('id')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('urlToImage')
        date = news_item.get('publishedAt')
        
    if image:
        news_result = News(id,author,title,description,url,image,date)
        news_object.append(news_result)    
        
        
        
    return news_object