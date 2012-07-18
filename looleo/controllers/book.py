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

from agiliza.utils import slugify

from looleo.managers import BookManager, UserManager
from looleo.managers import User, Book, Review
from looleo.managers import get_book_manager, get_user_manager

            
class Book(Controller):

	def get(self, request, params):
		bm = get_book_manager() 
		
		slug = params["book_slug"]
		data = {
			"book" : bm.findOneBook({"slug":slug}),
			}
		
		return data
		
	def post(self, request, params):
		bm = get_book_manager()
		if request.meta.has_key('title') and request.meta.has_key('author'):
			
			book = bm.createBook({
				"title":request.meta["title"],
				"author":request.meta["author"],
				"slug":slugify(request.meta["title"]),
			})
			id_book = bm.insertBook(book)
			
			if id_book is not None:
				return {
					"book":book,
					"msg":"Created successfully.",
				}

		return {
			"book":None,
			"msg":"Something was wrong.",
		}    
    
