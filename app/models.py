class Source:
    '''
    Source class to define news objects (sources)
    '''
    def __init__ (self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Articles:
    '''
    Articles class to define Articles objects
    '''
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt