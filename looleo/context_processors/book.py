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

from json import dumps

from agiliza.controllers import Controller
from agiliza.http import HttpResponseNotFound
from agiliza.utils import slugify
from agiliza.core.config import ConfigRunner

from looleo.managers import BookManager, UserManager
from looleo.managers import User, Book, Review
from looleo.managers import get_book_manager, get_user_manager

from looleo.utils import not_empty
from looleo.utils import who_is_logged

def ultimos_3_libros(request, params):
		
		bm = get_book_manager() 
		
		cursor = bm.findBooks()
		
		if cursor.count() > 3:
			return {
				"books" : cursor[cursor.count()-3:],
			}
		else:
			return {
				"books" : cursor[:cursor.count()],
			}
		
		
def ultimos_10_libros(request, params):
		
		bm = get_book_manager() 
		
		cursor = bm.findBooks()
		
		if cursor.count() > 10:			
			return {
				"books" : cursor[cursor.count()-10:],
			}
		else:
			return {
				"books" : cursor[:cursor.count()],
			}
		
def ultimos_12_libros(request, params):
		
		bm = get_book_manager() 
		
		cursor = bm.findBooks()
		
		if cursor.count() > 12:
			return {
				"books" : cursor[cursor.count()-12:],
			}
		else:
			return {
				"books" : cursor[:cursor.count()],
			}

def import_dumps(request, params):
	return {
		"dumps" : dumps,
		"str" : str,
		}

"""			
	def post(self, request, params):
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
			not_empty(request.data["text"].value) and
			'stars' in request.data and
			not_empty(request.data["stars"].value)): 
			
			
			review = Review({
				"user" : user,
				"book" : book,
				"text" : request.data["text"].value,
				"stars" : request.data["stars"].value,
				})
				
			user = um.addReview(review)
			book = bm.addReview(review)
			
			return {
				"book": book,
				"user_logged": True,
				"msg": "Comentario guardado correctamente.",
				}
					
		return {
			"book": book,
			"user_logged": True,
			"review_form":review,
			"msg":"Algunos campos del comentario no son válidos.",
		}
		

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
				
				# Si el libro no existía guardamos la imagen
				config = ConfigRunner()
				media_root = config.media_root
				media_url = config.media_url
				
				#Si existe, guardamos imagen.
				if "cover" in request.data:
					print("DIR COVER: ", dir(request.data["cover"]))
					print("DIR FILE: ", dir(request.data["cover"].file))
					file_name_server = book["slug"] + "." + request.data["cover"].filename.split(".")[-1]
					file = open(media_root + file_name_server, "wb")
					urlfile = media_url + file_name_server 
					for line in request.data["cover"].file:
						file.write(line)
					
					file.close()
					book["urlfile"] = urlfile
					print("Guardado con éxito! ------- %s ------" % urlfile)
				
				
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
"""
