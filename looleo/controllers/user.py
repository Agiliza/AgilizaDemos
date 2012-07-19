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
from agiliza.http import HttpResponseFound
from agiliza.utils import slugify

from looleo.managers import BookManager, UserManager
from looleo.managers import User, Book, Review
from looleo.managers import get_book_manager, get_user_manager

from looleo.utils import not_empty
from looleo.utils import who_is_logged

            
class User(Controller):

	def get(self, request, params):
		um = get_user_manager() 
		
		user = um.findOneUser({"username":params["username"]})
		if user is not None:
			return {
			"user" : user,
			}
			
		else:
			raise HttpResponseNotFound("El usuario con el nombre de usuario \
			 '%s' no existe." % params["username"])

class UserCreator(Controller):
	def get(self, request, params):
		return {}
		
	def post(self, request, params):
		um = get_user_manager()
		
		if ('username' in request.data and
			not_empty(request.data["username"].value) and
			'password' in request.data and
			not_empty(request.data["password"].value) and
			'email' in request.data and
			not_empty(request.data["email"].value)):
			
			user_exist = um.findOneUser(
				{"username":request.data["username"].value}
				)
				
			user_exist_mail = um.findOneUser(
				{"email":request.data["email"].value}
				)
				
			if user_exist is None and user_exist_mail is None:
				
				user = um.createUser({
					"username":request.data["username"].value,
					"password":request.data["password"].value,
					"email":request.data["email"].value,
				})
				
				id_user = um.insertUser(user)
				
				if id_user is not None:
					return {
						"user":user,
						"msg":"Usuario creado satisfactoriamente.",
					}
				else:
					return {
						"user":None,
						"msg":"Algo ha ido mal. Inténtelo de nuevo.",
					}			
					
			else:
				if user_exist:
					return {
						"msg":"Ya existe un usuario con el nombre de usuario \
						'%s'." % request.data["username"].value,
					}
					
				elif user_exist_mail:
					return {
						"msg": "El email '%s' ya está registrado." % request.data["email"].value,
					}

		else:
			return {
				"user":None,
				"msg":"Falta alguno de los campos requeridos.",
			}
		
		
class UserLogin(Controller):

	def get(self, request, params):
		user = who_is_logged(self.session)
		if user is not None:
			return HttpResponseFound(redirect_to=("/user/%s/" % user["username"]))
		return {}

	def post(self, request, params):
		user = who_is_logged(self.session)
		if user is not None:
			return HttpResponseFound(redirect_to=("/user/%s/" % user["username"]))
		
		um = get_user_manager()
		
		if ("username" in request.data and
			not_empty(request.data["username"].value) and
			"password" in request.data and
			not_empty(request.data["password"].value)):
			
			user = um.findOneUser({
				"username":request.data["username"].value,
				"password":request.data["password"].value,
			})
			
			if user is not None:
				print("SID: ", self.session["sid"])
				self.session["user_logged"] = str(request.data["username"].value)
				return HttpResponseFound(
					redirect_to="/user/%s/" % user["username"]
					)
					
		return {
			"user":None,
			"msg":"Usuario y contraseña incorrectos."
		}
	
class UserLogout(Controller):
	
	def get(self, request, params):
		user = who_is_logged(self.session)
		if user is not None:
			del self.session["user_logged"]
			
		return HttpResponseFound(redirect_to="/")
    
