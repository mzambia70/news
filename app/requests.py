import urllib.request,json
from .models import Source,Articles

#Getting api_key
api_key = None
#Getting the base_url
base_url = None
#Getting source_url
source_url = None

def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_API_URL']
    source_url = app.config['SOURCE_NEWS_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        source_results = None

            #urllib opens and reads URLs
        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_sources(source_results_list)
    return source_results

def process_sources(source_list):
    """
    Function that processes new list dictionary and turns them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain news sources_list
    Returns:
        news_results: A list of news objects
    """
    news_results = []
    for source in source_list:
        id = source.get('id')

        name = source.get('name')

        description = source.get('description')
        url = source.get('url')
        category = source.get('category')

        if url:
            source_object = Source(id,name,description,url,category)

            news_results.append(source_object)
    return news_results

def get_articles(id):
    """
    Function that gets the json response to our url request
    """
    get_sources_news_url = source_url.format(id,api_key)
    with urllib.request.urlopen(get_sources_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)

    return news_results


def process_articles(articles_list):
    """
    Function that processes new list dictionary and turns them to a list of objects
    Args:
        news_list: A list of dictionaries that contain news sources_list
    Returns:
        news_results: A list of news objects
    """
    news_results = []
    source_dictionary = {}
    for result in articles_list:
        # source_dictionary['id'] = source_id['id']
        # id = source_dictionary['id']
        #store the nested dictionary in source_id

        source_id = result['source']['id']
        #extrect and store it in our source dictionary
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            source_object = Articles(id,author,title,description,url,urlToImage, publishedAt)
            news_results.append(source_object)

    return news_results