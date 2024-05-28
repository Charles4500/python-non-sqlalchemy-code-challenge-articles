class Article:
    def __init__(self, author, magazine, title):
        
        
        assert isinstance(author, Author)
        assert isinstance(magazine, Magazine)
        assert 5 <= len(title) <= 50
        assert isinstance(title,str)
        
        self._author = author
        self._magazine = magazine
        self._title = title

        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, value):
        assert isinstance(value, Author)
        
        self._author = value

    @magazine.setter
    def magazine(self, value):
        assert isinstance(value, Magazine)
           
        self._magazine = value
    
class Author:
    def __init__(self, name):
        assert isinstance(name, str) or len(name) == 0
       
           
        self._name = name
        self._articles = []
          
    @property
    def name(self):
        return self._name

    def add_article(self, article):
        assert isinstance(article, Article)
          
        self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))
            
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str) or not (2 <= len(value) <= 16)
           
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        assert isinstance(value, str) or len(value) == 0
           
        self._category = value

    def add_article(self, article):
        assert isinstance(article, Article)
        
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))
    
author = Author("John Doe")
magazine = Magazine("Tech Today", "Technology")
article = Article(author, magazine, "The Future of AI")

print(author.name) 
print(magazine.name)  
print(article.title) 




