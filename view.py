from django.http import HTTPResponse
print('123')

def index():
    return HTTPResponse('index')
