"""
This file is part of Agiliza.

Agiliza is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Agiliza is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Agiliza.  If not, see <http://www.gnu.org/licenses/>.


Copyright (c) 2012 Álvaro Hurtado <alvarohurtado84@gmail.com>
"""

from agiliza.controllers import Controller

from looleo.managers import BookManager, UserManager
from looleo.managers import User, Book, Review


class BookReviews(Controller):
    
    def get(self, request, params):
        bm = BookManager(
            database_name="looleo_prueba",
            collection_name="prueba"
            )
        slug = params["book_slug"]
        data = {
            "book" : bm.findOneBook({"slug":slug}),
            }
        
        return data
        
    def post(self, request, params):
        return {}
        
        
    
    