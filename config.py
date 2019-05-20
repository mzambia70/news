import os #enabling our app to interact with os dependant functionalty


class Config:
  '''
  General configuration parent class
  '''
  pass
  NEWS_SOURCSES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
  NEWS_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey= {}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  '''
  productoin configuration child class
  
  Args:
       config: the parent configuratoin class with General configuration settings
  '''
  pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
# enabling the debug mode in our app
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}