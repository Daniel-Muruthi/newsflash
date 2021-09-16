import unittest
from news import NewsSources, News, SearchNewsAll



class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("cnn-news","CNN NEWS","Leftist deepstate run media station","https://www.cnn.com/", "https://image.cnn/2", "content", "Daniel", "2021-09-16T13:06:07Z")
        self.new_sources = NewsSources("abc-news", "ABC News", "Another deepstate leftist run big media station", "http://abc.com")
        self.new_search = SearchNewsAll("US unemployment claims","CNN NEWS","Leftist deepstate run media station","https://www.cnn.com/", "https://image.cnn/2", "content", "Daniel", "2021-09-16T13:06:07Z")

    def test_instance(self):
        """
        Test case method to check if self.new_news, self.new_sources, self.new_search are instances of News, NewsSources and SearchNewsAll rspectively """
        self.assertTrue(isinstance(self.new_news,News))
        self.assertTrue(isinstance(self.new_sources,NewsSources))
        self.assertTrue(isinstance(self.new_search,SearchNewsAll))


    def test_instanciation(self):
        '''
        This test case method will test that our new Object in setUp has been instanciated properly
        '''
        #self.new_news
        self.assertEqual(self.new_news.title, "cnn-news")
        self.assertEqual(self.new_news.name, "CNN NEWS")
        self.assertEqual(self.new_news.description, "Leftist deepstate run media station")
        self.assertEqual(self.new_news.url, "https://www.cnn.com/")
        self.assertEqual(self.new_news.urlToImage, "https://image.cnn/2")
        self.assertEqual(self.new_news.content, "content")
        self.assertEqual(self.new_news.author, "Daniel")
        self.assertEqual(self.new_news.publishedAt, "2021-09-16T13:06:07Z")

        #self.new_sources
        self.assertEqual(self.new_sources.id, "abc-news")
        self.assertEqual(self.new_sources.name, "ABC News")
        self.assertEqual(self.new_sources.description, "Another deepstate leftist run big media station")
        self.assertEqual(self.new_sources.url, "http://abc.com")

        #self.news_search
        self.assertEqual(self.new_search.title, "US unemployment claims")
        self.assertEqual(self.new_search.name, "CNN NEWS")
        self.assertEqual(self.new_search.description, "Leftist deepstate run media station")
        self.assertEqual(self.new_search.url, "https://www.cnn.com/")
        self.assertEqual(self.new_search.urlToImage, "https://image.cnn/2")
        self.assertEqual(self.new_search.content, "content")
        self.assertEqual(self.new_search.author, "Daniel")
        self.assertEqual(self.new_search.publishedAt, "2021-09-16T13:06:07Z")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        NewsSources.new_sources = []
        News.new_news = []
        SearchNewsAll.new_search = []


if __name__ == '__main__':
    unittest.main()