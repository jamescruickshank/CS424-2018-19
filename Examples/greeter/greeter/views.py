from django.http import HttpResponse

from IPython import embed


def index(request,name):
    #embed()
    if name =="Trump" or name=="Obama":
        return HttpResponse("Get the hell outta here!")
    response = HttpResponse("Welcome %s!"%name)
    return response
