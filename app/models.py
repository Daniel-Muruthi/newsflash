class News_Source:
    """
    News_Source class to define news source objects
    """
    #id might be source.id

    def __init__(self, id, url):
        self.id = id
        self.url = url


class News_Article:

    news_article_info = []

    def __init__(self, title, description, urlToImage, content):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content