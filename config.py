import os

class Config:
    '''
    General configuration parent class
    '''
    pass

    NEWS_BASE_API_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey=35c7d8f389324702bf046aae6f6fc72e'
    SOURCE_NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=35c7d8f389324702bf046aae6f6fc72e'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('9\xc52\xac\x8b\xb0\x9f\xc6\xf6\xda')



class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}