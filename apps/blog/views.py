from agiliza.views import View


class EntryView(View):
    def urls(self):
        return (
            url(r'^$'),

            url(r'^list/', 'list'),
            url(r'^list/page/<page>/', 'list'),

            url(r'^list/<year>/', 'list'),
            url(r'^list/<year>/page/<page>/', 'list'),

            url(r'^list/<year>/<month>/', 'list'),
            url(r'^list/<year>/<month>/page/<page>/', 'list'),

            url(r'^list/<year>/<month>/<day>/', 'list'),
            url(r'^list/<year>/<month>/<day>/page/<page>/', 'list'),

            url(r'^entry/', 'entry'),
            url(r'^entry/<slug>/', 'entry'),
        )

    def get(self):
        """Most important entry list"""
        context_data = self.request.query
        return context_data, templates

    def get_list(self, page=1):
        """Retrieve a page of full entry list"""
        return context_data, templates

    def post_list(self):
        """Modify entry list parameters. For example: items per page"""
        return context_data, templates

    def get_entry(self, slug):
        """Retrieve the entry identified by ``slug``"""
        return context_data, templates

    def post_entry(self, slug):
        """Modify the entry identified by ``slug``"""
        return context_data, templates

    def put_entry(self):
        """Create a new entry"""
        return context_data, templates

    def delete_entry(self, slug):
        """Delete the entry identified by ``slug``"""
        return context_data, templates

