from django.shortcuts import render, redirect, HttpResponse 
from django.core.paginator import Paginator
from .models import Product,Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

def home(req):
    product_info = Product.objects.all()
    print(product_info)
    return render(req, 'test1/home.html', {'product_info':product_info})
    # return HttpResponse('Home Page')

def contact(req):
    if req.method == 'GET':
        return render(req, 'test1/contact.html')
    else:
        x = req.POST.get("name")
        y = req.POST.get("email")
        z = req.POST.get("message")
        new_data = Contact(name=x, email=y, message=z)
        new_data.save()
        return render(req, 'test1/contact.html', {'success':'Query sent successfully!'})
    

def about(req):
    return render(req, 'test1/about.html')

@login_required(login_url='loginUser')
def products(req):
    myProducts = Product.objects.all()
    paginator = Paginator(myProducts, 3)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(req, 'test1/product.html', {"page_obj": page_obj})


def findProduct(req):
    if(req.method == 'POST'):
        x = req.POST.get('product_search')
        # print(x)
        mydata = Product.objects.filter(Q(product_name__icontains = x)|Q(product_category__icontains = x)|Q(product_id__icontains = x))
        # print(mydata)
        if mydata:
            return render(req, 'test1/home.html', {'product_info':mydata})
        else:
            return render(req, 'test1/home.html', {'warning':'No such product found! Try something else...'})


def loginUser(req):
    if(req.method == 'GET'):
        return render(req, 'test1/loginUser.html', {'form':AuthenticationForm()})
    elif(req.method == 'POST'):
        u = req.POST.get('username')
        p = req.POST.get('password')
        user = authenticate(req, username=u, password=p)
        if user is None:
            return render(req, 'test1/loginUser.html', {'form':AuthenticationForm(), 'error':'Invalid Credentials!'})
        else:
            login(req, user)
            return redirect('home')
    
def signUpUser(req):
    if(req.method == 'GET'):
        return render(req, 'test1/signUpUser.html', {'form':UserCreationForm()})
    else:
        #find the names using insepct
        u = req.POST.get('username')
        p1 = req.POST.get('password1')
        p2 = req.POST.get('password2')
        
        # check if the passwords are same
        if(p1 == p2):
            # check if username already exists
            if(User.objects.filter(username = u)):
                return render(req, 'test1/signUpUser.html', {'form':UserCreationForm(), 'error':'Username already exists! Try again!'})
            else:
                user = User.objects.create_user(username=u, password=p1)
                user.save()
                login(req, user)
                return redirect('home')
        
        else:
            # password mismatch error
            return render(req, 'test1/signUpUser.html', {'form':UserCreationForm(), 'error':'Password Mismatch! Try again!'})
        
    

def logOutUser(req):
    if(req.method == 'GET'):
        logout(req)
        return redirect('home')
    


