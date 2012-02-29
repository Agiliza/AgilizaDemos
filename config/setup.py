from agiliza.conf import settings
from apps import static


mongodb_database = {
    'engine': 'agiliza.core.backends.databases.mongodb',
    'host': 'localhost',
    'name': 'mydatabase',
    'options': {},
    'password': 'mypassword',
    'port': 80,
    'user': 'myuser',
}


# Register apps for all profiles
settings.apps.register(static)

#settings.profiles.create('debug')
#debug = settings.profiles.get('debug')
#debug.databases.register(name='default', options=mongodb_database)
#debug.databases['default']

settings.databases.register(mongodb_database, name='default')
# settings.databases['default']
