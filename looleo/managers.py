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


Copyright (c) 2012 Alvaro Hurtado <alvarohurtado84@gmail.com>
"""

from pymongo import Connection

from agiliza.core.utils.patterns import Singleton

from bson.objectid import ObjectId

class NiceDict(dict):
	def __getattr__(self, key):
		if key not in self.keys():
			return getattr(super(NiceDict, self),key)
		return self[key]

	def __setattr__(self, key, value):
		if key not in self.keys():
			return setattr(super(NiceDict, self), key, value)
		self[key] = value


class PymongoManager(Singleton):
	def __init__(self, database_name, collection_name, host=None, port=None):
		if not host or not port:
			self.connection = Connection()
		else:
			self.connection = Connection(host=host, port=port)
		self.db = getattr(self.connection, database_name)
		self.collection = getattr(self.db, collection_name)


class UserManager(PymongoManager):
	def __init__(self, *args, **kwargs):
		super(UserManager, self).__init__(*args, **kwargs)

	def insertUser(self, user):
		if user.is_valid():
			return self.collection.insert(user)
		else:
			return None

	def createUser(self, *args, **kwargs):
		user = User(*args, **kwargs)
		if user.is_valid():
			return user
		else:
			return None

	def findOneUser(self, document=None):
		query = {}
		if document is not None:
			query.update(document)
		query.update({"type":"user"})

		return self.collection.find_one(query)

	def findUsers(self, document=None):
		query = {}
		if document is not None:
			query.update(document)
		query.update({"type":"user"})

		return self.collection.find(query)

	def addReview(self, review):
		user = self.findOneUser({"_id":review.user["_id"]})

		rev = {"text":review.text,
				"book":{
					"_id":review.book["_id"],
					"title":review.book["title"],
					"author":review.book["author"],
				},
				"stars":review.stars,
				"_id":review._id,}

		if user.has_key("review"):
			user["review"].append(rev)
		else:
			user.update({"review":[rev]})

		self.collection.update(
			{"_id":user["_id"]},
			user
		)



class BookManager(PymongoManager):
	def __init__(self, *args, **kwargs):
		super(BookManager, self).__init__(*args, **kwargs)

	def insertBook(self, book):
		if book.is_valid():
			return self.collection.insert(book)
		else:
			return None

	def createBook(self, *args, **kwargs):
		book = Book(*args, **kwargs)
		if book.is_valid():
			return book
		else:
			return None

	def findOneBook(self, document=None):
		query = {}
		if document is not None:
			query.update(document)
		query.update({"type":"book"})

		return self.collection.find_one(query)

	def findBooks(self, document):
		query = {}
		if document is not None:
			query.update(document)
		query.update({"type":"book"})

		return self.collection.find(query)

	def addReview(self, review):
		book = self.findOneBook({"_id":review.book["_id"]})

		rev = {"text":review.text,
				"user":{
					"_id":review.user["_id"],
					"username":review.user["username"],
					"email":review.user["email"],
				},
				"stars":review.stars,
				"_id":review._id,}

		if book.has_key("review"):
			book["review"].append(rev)
		else:
			book.update({"review":[rev]})

		self.collection.update(
			{"_id":book["_id"]},
			book
		)

class User(NiceDict):
	def __init__(self, *args, **kwargs):
		super(User, self).__init__(*args, **kwargs)
		self.update({"type":"user"})


	def is_valid(self):
		required_fields = ("username", "password", "email")
		for rf in required_fields:
			try:
				getattr(self, rf)
			except AttributeError:
				return False
		return True

class Book(NiceDict):
	def __init__(self, *args, **kwargs):
		super(Book, self).__init__(*args, **kwargs)
		self.update({"type":"book"})

	def is_valid(self):
		required_fields = ("title", "author", "slug")
		for rf in required_fields:
			try:
				getattr(self, rf)
			except AttributeError:
				return False
		return True

class Review(NiceDict):
	def __init__(self, *args, **kwargs):
		super(Review, self).__init__(*args, **kwargs)
		self.update({"_id":ObjectId()})

	def is_valid(self):
		required_fields = ("text", "book", "user", "stars")
		for rf in required_fields:
			try:
				getattr(self, rf)
			except AttributeError:
				return False
		return True


def get_book_manager():
	return BookManager(
		database_name="looleo_prueba",
		collection_name="looleo_data",
		)
		
def get_user_manager():
	return UserManager(
		database_name="looleo_prueba",
		collection_name="looleo_data",
		)
		
