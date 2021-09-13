class News:
    '''
    News class to define movie objects
    '''

    def __init__(self, id, title, description, urlToImage, content):
        self.id = id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        