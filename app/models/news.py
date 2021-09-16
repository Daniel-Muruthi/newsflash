class News:
    '''
    News class to define News Objects

    '''

    new_news = []

    def __init__(self,title,name,description,url,urlToImage,content,author,publishedAt):
        self.title =title
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.author= author
        self.publishedAt= publishedAt



class SearchNewsAll:
    """
    News class based on topic search
    """
    
    new_search = []
    def __init__(self,title,name,description,url,urlToImage,content,author,publishedAt):
        self.title =title
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.author= author
        self.publishedAt= publishedAt

        


class NewsSources:

    new_sources = []

    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


