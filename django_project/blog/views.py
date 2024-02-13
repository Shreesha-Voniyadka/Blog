from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
# Either render or shortcut


posts = [
        {
        'author':'Shreesha Voniyadka',
        'title':"Vlog1",
        'content':'First contetnt',
        'date_posted':'2/13/2024'
        },
        {
        'author':'John Doe',
        'title':"Vlogs2",
        'content':'Second contetnt',
        'date_posted':'2/13/2024'
        }
    ]

def home(request):
    context = {
        'posts':posts
    }
    # return HttpResponse('<h1> Blog Home</h1>')
    return render(request, 'blog/home.html',context)



def about(request):
    # return HttpResponse('<h1> Blog Home</h1>'
    return render(request, 'blog/about.html',{'title':'About'})