from django.http import HttpResponse

def index_view(response):
    return HttpResponse("<h1>Home Page</h1>")

def about_view(response):
    return HttpResponse("<h2>About</h2>")

def contact_view(response):
    return HttpResponse("<h2>Contact</h2>")

