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
  News class to define the News objects
  '''

  def __init__(self, id, author, title, description, image, url, date):
    self.id = id
    self.author = author
    self.title = title
    self.description = description
    self.image = image
    self.url = url
    self. date = date