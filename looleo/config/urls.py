
from agiliza.config.urls import url, include


url_patterns = (
    #url("app/", include("app.config.url")),
    url("/book/(?P<book_slug>[-\w_]+)/", "looleo.controllers.Book", name="book_reviews"),
    url("/book/", "looleo.controllers.BookCreator", name="book"),
    
    url("/user/login/", "looleo.controllers.UserLogin", name="user_login"),
    url("/user/logout/", "looleo.controllers.UserLogout", name="user_logout"),
    url("/user/(?P<username>[-\w_]+)/", "looleo.controllers.User", name="user_reviews"),
    url("/user/", "looleo.controllers.UserCreator", name="user"),
    
    #url("/", "looleo.controllers.Home", name="home"),
)

