#!/usr/bin/python
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf

URL = 'http://127.0.0.1:8888'


class Handler(object):
    def __init__(self, builder, data):
        self.window = builder.get_object("window1")
        self.title_label = builder.get_object("label1")
        self.author_label = builder.get_object("label2")
        self.cover_image = builder.get_object("image1")
        self.statusbar = builder.get_object("statusbar1")
        self.reviews_treeview = builder.get_object("treeview1")

        self.window.set_title('Looleo GTK')
        self.create_treeview_columns(self.reviews_treeview)
        self.reviews_treeview.connect("row-activated", self.on_activated)

        self.data = data
        self.position = 0

        self.display_book()

    def create_treeview_columns(self, treeview):
        renderer_text = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Stars", renderer_text, text=0)
        column.set_sort_column_id(0) # Ordenable por la columna 0
        treeview.append_column(column)

        renderer_text = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("User", renderer_text, text=1)
        column.set_sort_column_id(1) # Ordenable por la columna 1
        treeview.append_column(column)

        renderer_text = Gtk.CellRendererText()
        renderer_text.props.wrap_width = 200
        column = Gtk.TreeViewColumn("Review", renderer_text, text=2, background=3)
        treeview.append_column(column)

    def display_book(self):
        book = self.data[self.position]

        width, height = 200, 300
        pixbuf = Pixbuf.new_from_file_at_size(book['file'], width, height)

        self.title_label.set_text(book['title'])
        self.author_label.set_text(book['author'])
        self.cover_image.set_from_pixbuf(pixbuf)

        liststore = Gtk.ListStore(str, str, str, str)
        if 'reviews' in book:
            for review in book['reviews']:
                liststore.append((
                    review['stars'],
                    review['user']['username'],
                    review['text'],
                    '#E6E1CF',
                ))
        self.reviews_treeview.set_model(liststore)

        self.statusbar.push(0, 'Cargado el libro: %s' % book['title'])

    def on_activated(self, widget, row, col):

        model = widget.get_model()
        text = "Review: %s, %s, %s" % (model[row][0], model[row][1], model[row][2])
        self.statusbar.push(0, text)

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def leftPressed(self, button):
        if self.position <= 0:
            return

        self.position -= 1
        self.display_book()

    def rightPressed(self, button):
        if self.position >= len(self.data)-1:
            return

        self.position += 1
        self.display_book()


def get_data(url):
    import json
    from urllib2 import Request
    from urllib2 import urlopen

    request = Request(url)
    request.add_header("accept", "application/json")

    response = urlopen(request)
    text = response.read()

    return json.loads(text)

def get_image(url):
    import json
    from urllib2 import Request
    from urllib2 import urlopen

    request = Request(url)
    response = urlopen(request)

    return response.read()

def get_images(data):
    import os

    for book in data:
        url = book['urlfile']
        name = url.replace('/media/', 'images/')
        book['file'] = name
        if os.path.isfile(name):
            continue

        with open(name, 'wb') as f:
            f.write(get_image(URL + url))




if __name__ == "__main__":
    data = (
        {
            'title': 'libro1',
            'author': 'autor1',
            'urlfile': 'link/1984.jpg',
            'file': 'images/1984.jpg',
            'reviews': (
                {
                    "text": "el libro 1 es muuu bueno",
                    "book": "libro1",
                    "user": "reviewer1",
                    "stars": 5,
                },
                {
                    "text": "el libro 1 es una basura",
                    "book": "libro1",
                    "user": "reviewer2",
                    "stars": 0,
                },
            ),
        },
        {
            'title': 'libro2',
            'author': 'autor2',
            'urlfile': 'link/en-llamas.jpg',
            'file': 'images/en-llamas.jpg',
            'reviews': (),
        },

    )
    data = get_data(URL)
    get_images(data)
    builder = Gtk.Builder()
    builder.add_from_file("ui/simple.glade")
    builder.connect_signals(Handler(builder, data))

    window = builder.get_object("window1")

    window.show_all()

    Gtk.main()
