#from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Clothing

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def enter(request):
    template = loader.get_template('enter.html')
    return HttpResponse(template.render({}, request))

def jackets(request):
    template = loader.get_template('jackets.html')
    return HttpResponse(template.render({}, request))

def addjackets(request):
    x = request.POST['jackets']
    clothing = Clothing(jackets=x)
    clothing.save()
    return HttpResponseRedirect(reverse('jackets'))

def shirts(request):
    template = loader.get_template('shirts.html')
    return HttpResponse(template.render({}, request))

def addshirts(request):
    x = request.POST['shirts']
    clothing = Clothing(shirts=x)
    clothing.save()
    return HttpResponseRedirect(reverse('shirts'))

def pants(request):
    template = loader.get_template('pants.html')
    return HttpResponse(template.render({}, request))

def addpants(request):
    x = request.POST['pants']
    clothing = Clothing(pants=x)
    clothing.save()
    return HttpResponseRedirect(reverse('pants'))

def shoes(request):
    template = loader.get_template('shoes.html')
    return HttpResponse(template.render({}, request))

def addshoes(request):
    x = request.POST['shoes']
    clothing = Clothing(shoes=x)
    clothing.save()
    return HttpResponseRedirect(reverse('shoes'))

def list(request):
    template = loader.get_template('list.html')
    return HttpResponse(template.render({}, request))

def viewjackets(request):
    myjackets = Clothing.objects.values_list('jackets')
    template = loader.get_template('viewjackets.html')
    context = {
        'clothing': myjackets,
    }
    return HttpResponse(template.render(context, request))

def viewshirts(request):
    myshirts = Clothing.objects.values_list('shirts')
    template = loader.get_template('viewshirts.html')
    context = {
        'clothing': myshirts,
    }
    return HttpResponse(template.render(context, request))

def viewpants(request):
    mypants = Clothing.objects.values_list('pants')
    template = loader.get_template('viewpants.html')
    context = {
        'clothing': mypants,
    }
    return HttpResponse(template.render(context, request))

def viewshoes(request):
    myshoes = Clothing.objects.values_list('shoes')
    template = loader.get_template('viewshoes.html')
    context = {
        'clothing': myshoes,
    }
    return HttpResponse(template.render(context, request))

def delete(request):
    template = loader.get_template('delete.html')
    return HttpResponse(template.render({}, request))

def deletejackets(request):
    myjackets = Clothing.objects.values_list('jackets')
    template = loader.get_template('deletejackets.html')
    context = {
        'clothing': myjackets,
    }
    return HttpResponse(template.render(context, request))

##def deletethatjacket(request, jackets):
##    jacket = Clothing.objects.get(jackets=jackets)
##    jacket.delete()
##    return HttpResponseRedirect(reverse('deletejackets'))

def deleteshirts(request):
    myshirts = Clothing.objects.values_list('shirts')
    template = loader.get_template('deleteshirts.html')
    context = {
        'clothing': myshirts,
    }
    return HttpResponse(template.render(context, request))

def deletepants(request):
    mypants = Clothing.objects.values_list('pants')
    template = loader.get_template('deletepants.html')
    context = {
        'clothing': mypants,
    }
    return HttpResponse(template.render(context, request))

def deleteshoes(request):
    myshoes = Clothing.objects.values_list('shoes')
    template = loader.get_template('deleteshoes.html')
    context = {
        'clothing': myshoes,
    }
    return HttpResponse(template.render(context, request))


##def deleteshirts(request):
##

##def deletepants(request):
##

##def deleteshoes(request):

    

    
