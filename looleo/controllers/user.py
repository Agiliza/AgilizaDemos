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

            
class User(Controller):

	def get(self, request, params):
		um = get_user_manager() 
		
		username = params["username"]
		return {
			"user" : um.findOneUser({"username":username}),
			}

class UserCreator(Controller):

	def post(self, request, params):
		um = get_user_manager()
		
		if 'username' in request.data and 'password' in request.data and 'email' in request.data:
			
			user = um.createUser({
				"username":request.data["username"].value,
				"password":request.data["password"].value,
				"email":request.data["email"].value,
			})
			
			id_user = um.insertUser(user)
			
			if id_user is not None:
				return {
					"user":user,
					"msg":"Created successfully.",
				}

		return {
			"user":None,
			"msg":"Something was wrong.",
		}
		
		
class UserLogin(Controller):

	def post(self, request, params):
		um = get_user_manager()
		
		if "username" in request.data and "password" in request.data:
			user = um.findOneUser({
				"username":request.data["username"].value,
				"password":request.data["password"].value,
			})
			
			if user is not None:
				# TODO METER EN SESSION
				return {
					"user":user,
					"msg":"Succeful login."
				}
		
		# QUITAR USUARIO DE SESSION
		return {
			"user":None,
			"msg":"Something was wrong."
		}
	
    
