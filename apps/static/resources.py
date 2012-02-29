from agiliza.http import HttpResponseOk
from agiliza.resources import Resource


class Main(Resource):
    @method(allow='GET')
    def get(self, request):
        form = '''
        <html><head></head>
        <body>
        <h1>Main - Test</h1>
        <p>%s</p>
        </body>
        </html>
        ''' % request.query
        return HttpResponseOk(content=form)

