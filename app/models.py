class Source:
    '''
    news_Source class to define News Source Objects
    '''
    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name =name
        self.description =description
        self.url =url
        self.category =category
        self.country =country


class Article:
    '''
    Article class to define News Articles Objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt



# class Sources:
# def __init__(self,id,name,description,language):
#     self.id=id
#     self.name=name
#     self.description=description
#     self.language=language
# class Articles:
# def __init__(self,author,title,description,url,publishedAt,urlToImage):
#     self.author=author
#     self.title=title
#     self.description=description
#     self.url=url
#     self.publishedAt=publishedAt
#     self.urlToImage=urlToImage

