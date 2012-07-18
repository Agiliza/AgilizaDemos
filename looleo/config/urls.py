
from agiliza.config.urls import url, include


url_patterns = (
    #url("app/", include("app.config.url")),
    url("/book/(?P<book_slug>[\w_]+)/", "looleo.controllers.Book", name="book"),
)


