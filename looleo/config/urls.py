
from agiliza.config.urls import url, include


url_patterns = (
    #url("app/", include("app.config.url")),
    url("/reviews/(?P<book_slug>[\w_]+)/", "looleo.controllers.BookReviews", name="book-reviews"),
)


