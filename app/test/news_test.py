import unittest
from models import news
News = news.News

class NewsTest (unittest.TestCase):
    '''
    Test class to test the behaviour of the News Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News()

    def test_instance(self):
        self.assertTrue (isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()