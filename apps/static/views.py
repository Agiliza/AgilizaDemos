from agiliza.views import View


class MainView(View):
    def urls(self):
        return (
            url(r'^$')
        )

    def get(self):
        context_data = self.request.query
        return context_data, templates

