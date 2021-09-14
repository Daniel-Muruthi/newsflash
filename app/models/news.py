class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class SearchNewsAll:
    """
    News class based on topic search
    """
    

    def __init__(self,title,name,description,url,urlToImage,content,author):
        self.title =title
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.author= author
