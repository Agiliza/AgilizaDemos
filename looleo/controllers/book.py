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
from agiliza.http import HttpResponseNotFound
from agiliza.utils import slugify

from looleo.managers import BookManager, UserManager
from looleo.managers import User, Book, Review
from looleo.managers import get_book_manager, get_user_manager

from looleo.utils import not_empty
from looleo.utils import who_is_logged

            
class Book(Controller):


	def get(self, request, params):
		#print("LOGGED USER IS ", who_is_logged(self.session))
		#if not "count" in self.session:
			#self.session["count"] = 1
		#else:
			#self.session["count"] = self.session["count"] + 1
			
		#print("SID: ", self.session["sid"])	
		#print("IS")
		#print("IS")
		#print("IS")
		#if "user_logged" in self.session:
			#print("ONLINE: ", self.session["user_logged"])
		#print("IS")
		#print("IS")
		#print("IS")

		#
		#print("Cookies: ", request.cookies)
		#if request.cookies.get("sid2"):
		#	self.cookies["sid2"] = ""
		#	self.cookies["sid2"]["expires"]="10-jul-2010 20:54:21 GMT"
		#
		#if request.cookies.get("sid"):
		#	self.cookies["dis"]="pinocho"
		#
		
		bm = get_book_manager() 
		
		slug = params["book_slug"]
		book = bm.findOneBook({"slug":slug})
		
		user = who_is_logged(self.session)
		if user is None:
			user_logged = False
		else:
			user_logged = True
		
		if book is not None:
			return {
				"book" : bm.findOneBook({"slug":slug}),
				"user_logged" : user_logged,
				#"count" : self.session["count"],
				}
		else:
			raise HttpResponseNotFound("El libro con identificador %s no existe." % slug)

class BookCreator(Controller):
	def get(self, request, params):
		user = who_is_logged(self.session)
		if user is None:
			return HttpResponseFound(redirect_to=("/user/login/"))
			
		return {
		}

	def post(self, request, params):
		user = who_is_logged(self.session)
		if user is None:
			return HttpResponseFound(redirect_to=("/user/login/"))
			
		bm = get_book_manager()
				
		if ('title' in request.data and 'author' in request.data and 
			not_empty(request.data["title"].value) and
			not_empty(request.data["author"].value)):			

			book = bm.createBook({
				"title":request.data["title"].value,
				"author":request.data["author"].value,
				"slug":slugify(request.data["title"].value),
			})
			
			# Exist this book?
			exist_book = bm.findOneBook({"slug":book["slug"]})
			
			if exist_book is None:
				id_book = bm.insertBook(book)
				
				if id_book is not None:
					return {
						"book":book,
						"msg":"Creado de forma satisfactoria.",
					}
					
				else:
					return {
						"msg":"Algo falló, inténtelo de nuevo.",
					}
					
			else:
				return {
						"msg":"Ya existe un libro con el título '%s'." % request.data["title"].value,
				}
		
		else:
			return {
				"msg":"Falta alguno de los campos.",
			}
			
	def put(self, request, params):
		um = get_user_manager()
		bm = get_book_manager()
		
		# Comprobamos que el usuario esté logueado
		username = who_is_logged(self.session)
		if username is None: 
			return HttpResponseFound(redirect_to="/user/login/")
		else:
			user = um.findOneUser({"username":username})
			
		#Comprobamos que la página del libro sea correctas
		slug = params["book_slug"]
		book = bm.findOneBook({"slug":slug})
		if book is None:
			raise HttpResponseNotFound("El libro con identificador %s no existe." % slug)
			
		
		if ('text' in request.data and
			not_empty(request._data["text"].value) and
			'stars' in request.data and
			not_empty(request._data["stars"].value)): 
			
			review = Review({
				"user" : user,
				"book" : book,
				"text" : request.data["text"].value,
				"stars" : request.data["stars"].value,
				})
				
			user_result = um.addReview(review)
			book_result = bm.addReview(review)
			
			if user_result and book_result:
				return {
					"book": book,
					"msg": "Comentario guardado correctamente.",
					}
				
			return {
				"book":book,
				"review_form":review,
				"msg": "Algo fué mal, inténtelo de nuevo.",
				}
		
		return {
			"book": book,
			"review_form":review,
			"msg":"Algunos campos del comentario no son válidos.",
		}
		
