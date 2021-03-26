from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def unicorn(request):
    # Good way to do it
    
    request.session['f_name'] = request.POST['first_name']
    request.session['l_name'] = request.POST['last_name']
    request.session['food'] = request.POST['fav_food']
    # print(request.POST['first_name'])
    return redirect('/processed')

def processed(request):
    return redirect('/second')

def second(request):
    return render(request, 'unicorn.html')

def catch_all(request, url):
    return redirect('/unicorn')
