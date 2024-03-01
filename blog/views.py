from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from blog.models import Blog,Contact
# Create your views here.
def home(request):
    return render(request, 'index.html')
def bloghome(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'bloghome.html', context)
def blogpost(request , slug):
    blogs = Blog.objects.filter(slug=slug).first()
    context = {'blogs': blogs}
    return render(request, 'blogpost.html', context)

def contact(request):
    context = {'success': False}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        context = {'success': True}
        print("data added to the database")
    return render(request, 'contact.html' , context)
def search(request):
    return render(request, 'search.html')
def user(request):
    contacts = Contact.objects.all()
    context = {'users': contacts}
    return render(request, 'userData.html',context)