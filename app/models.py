class Sources:
    '''
    source class to define source Objects
    '''

    def __init__(self, id, name, description, category, country, language):
      self.id = id
      self.name = name
      self.description = description
      self.category = category
      self.country = country
      self.language = language


class News:
  '''
  news class to define news objects
  '''

  def __init__(self, id, author, title, descrption, url, image, date):
    self.id = id
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.image = image
    self.date = date