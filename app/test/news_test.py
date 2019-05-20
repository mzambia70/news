import unittest
from app.models import Sources
 


class SourcesTest(unittest.testCase):
  '''
  test Class to test the behaviour of the news class
  '''


  def setUp(self): #instantiate News class to make self.new_news object
    '''
    Set up method that will run before every Test
    '''
    self.new_sources = Sources('CNN','CNN NEWS','Cable News Network that is a leader in providing news worldwide','cnn.com','general','U.S.A','eng')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_sources,Sources)) #to check if the object is an instance of News class
    def test_to_check_instance_variables(self):
       self.assertEquals(self.new_source.id,'CNN')
       self.assertEquals(self.new_source.name,'CNN News')
       self.assertEquals(self.new_source.description,'Cable News Newtork that is a leader in providing news worldwide')
       self.assertEquals(self.new_source.url,'cnn.com')
       self.assertEquals(self.new_source.category,'general')
       self.assertEquals(self.new_source.country'U.S.A')
       self.assertEquals(self.new_source.language,'eng')

class ArticlesTest(unittest.TestCase):
   '''
   Test Class to test the behaviour of the News class
   '''

   def setUp(self):
       '''
       Set up method that will run before every Test
       '''
       self.new_news = News('CNN','YOLO','The tech scene in Africa-Is it the next big thing?','A look at various tech hubs in Africa and the impact they have on the worlds economy','techie.com','techie.com/7643t94.jpg','2019-04-14')

   def test_instance(self):
       self.assertTrue(isinstance(self.new_news,News))

   def test_to_check_instance_variables(self):
       self.assertEquals(self.new_news.id,'CNN')
       self.assertEquals(self.new_news.author,'YOLO')
       self.assertEquals(self.new_news.title,'The tech scene in Africa-Is it the next big thing?')
       self.assertEquals(self.new_news.description,'A look at various tech hubs in Africa and the impact they have on the worlds economy')
       self.assertEquals(self.new_news.url,'techie.com')
       self.assertEquals(self.new_news.image,'techie.com/7643t94.jpg')
       self.assertEquals(self.new_news.date,'2019-04-14')
# if __name__ = '__main__':
#   unittest.main()