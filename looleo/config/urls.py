
from agiliza.config.urls import url, include


url_patterns = (
    #url("app/", include("app.config.url")),
    url("/book/(?P<book_slug>[-\w_]+)/", "looleo.controllers.Book", name="book"),
    url("/book/", "looleo.controllers.BookCreator", name="book"),
    
    url("/user/login/", "looleo.controllers.UserLogin", name="user"),
    url("/user/(?P<username>[-\w_]+)/", "looleo.controllers.User", name="user"),
    url("/user/", "looleo.controllers.UserCreator", name="user"),
    
    url("/review/", "looleo.controllers.ReviewCreator", name="review"),
    
    #url("/", "looleo.controllers.home", name="home"),
)

