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
from agiliza.http import HttpResponseFound
from agiliza.utils import slugify

from looleo.managers import BookManager, UserManager
from looleo.managers import User, Book, Review
from looleo.managers import get_book_manager, get_user_manager


class ReviewCreator(Controller):

	def post(self, request, params):
		um = get_user_manager()
		bm = get_book_manager()
		
		if 'text' in request.data and 'stars' in request.data and 'book_slug' in request.data:
			
			# TODO user_id or username = FROM SESSION
			#user = um.findOneUser({"_id":user_id})
			#user = um.findOneUser({"username":username})
			
			book = bm.findOneBook({"slug":request.data["book_slug"].value})
			
			review = Review({
				"user" : user,
				"book" : book,
				"text" : request.data["text"].value,
				"stars" : request.data["stars"].value,
				})
				
			user_result = um.addReview(review)
			book_result = bm.addReview(review)
			
			if user_result and book_result:
				return HttpResponseFound(
					redirect_to = "/book/"+book["slug"]+"/"
					)
				
			return {
				"review":review,
				"msg": "Something was wrong",
				}
		
		return {
			"review":review,
			"msg":"Something is missing.",
		}
		
