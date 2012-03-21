from agiliza.views import View


class EntryView(View):
    def url_patterns(self):
        return (
            (r'^$', ''),

            (r'^list/', 'list'),
            (r'^list/page/(?P<page>\d+)/', 'list'),

            (r'^list/(?P<year>\d+)/', 'list'),
            (r'^list/(?P<year>\d+)/page/(?P<page>\d+)/', 'list'),

            (r'^list/(?P<year>\d+)/(?P<month>\d+)/', 'list'),
            (r'^list/(?P<year>\d+)/(?P<month>\d+)/page/(?P<page>\d+)/', 'list'),

            (r'^list/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', 'list'),
            (r'^list/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/page/(?P<page>\d+)/', 'list'),

            (r'^entry/', 'entry'),
            (r'^entry/(?P<slug>\w+)/', 'entry'),
        )

    def get(self):
        """Most important entry list"""
        context_data = 'get'
        templates = None
        return context_data, templates

    def get_list(self, page=1):
        """Retrieve a page of full entry list"""
        context_data = 'get_list'
        templates = None
        return context_data, templates

    def post_list(self):
        """Modify entry list parameters. For example: items per page"""
        context_data = 'post_list'
        templates = None
        return context_data, templates

    def get_entry(self, slug):
        """Retrieve the entry identified by ``slug``"""
        context_data = 'get_entry'
        templates = None
        return context_data, templates

    def post_entry(self, slug):
        """Modify the entry identified by ``slug``"""
        context_data = 'post_entry'
        templates = None
        return context_data, templates

    def put_entry(self):
        """Create a new entry"""
        context_data = 'put_entry'
        templates = None
        return context_data, templates

    def delete_entry(self, slug):
        """Delete the entry identified by ``slug``"""
        context_data = 'delete_entry'
        templates = None
        return context_data, templates

class FakeRequest(object):
    def __init__(self, method, meta):
        self.method = method
        self.meta = meta


view = EntryView()

r1 = FakeRequest('GET', {'path_info': 'list/page/3/'})
r2 = FakeRequest('GET', {'path_info': 'list/'})
cd, t = view.dispatch(r1, None, None, None)
print(cd + ' for: ' + r1.meta['path_info'])
cd, t = view.dispatch(r2, None, None, None)
print(cd + ' for: ' + r2.meta['path_info'])
