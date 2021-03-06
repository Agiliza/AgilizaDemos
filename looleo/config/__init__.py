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

installed_apps = []
middleware_level0 = ['agiliza.addons.sessions.middlewares.SessionMiddleware',
	'agiliza.addons.servingfiles.middlewares.ServingFilesMiddleware',
]
middleware_level1 = ['agiliza.addons.sessions.middlewares.SessionMiddleware']
templates = {
    'directory': './templates/'
}

media_url = "/media/"
media_root = "./media/"

static_url = "/static/"
static_root = "./static/"

settings = {
	'sessions':{
		'directory': './session/',
		#'domain':'localhost',
		'path':'/',
	}
}
