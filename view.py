from django.http import HTTPResponse


def index():
    return HTTPResponse('index')
