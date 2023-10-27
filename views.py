from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking,Profile
from math import ceil

customer ={'id': ' ',
                                'from': ' ',
                                'To': '',
                                'weight': '',
                                'price': ''}


def dashboard(request):
    return render(request,'dashboard.html',{'section':'dashboard'})
 
def index(request):
    return render(request,'index.html')
        
 
def search(request):
    return render(request,'search.html')
     

def about(request):
      return render(request,'about.html')

def services(request):
    return render(request,'services.html')




def order(request):
      return render(request,'order.html')

def submit(request):
      return render(request,'submit.html')


def contact(request):
    return render(request,'contact.html')
    
def user_login(request):
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                        password=cd['password'])
     
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated''successfully')
                else:
                  return HttpResponse('Disabled Account')
            else:
                 return HttpResponse('Invalid login')
    else:
        form=LoginForm()

    return render(request,'login.html',{'form':form})
            
     
def register(request):
    if request.method == 'POST':
          user_form = UserRegistrationForm(request.POST)
          if user_form.is_valid():
              new_user = user_form.save(commit=False)
              new_user.set_password(user_form.cleaned_data['password'])
              new_user.save()
              Profile.objects.create(user=new_user)
              return render(request,'register_done.html',{'new_user': new_user})
    else:
      user_form=UserRegistrationForm()
    return render(request,'register.html',{'user_form':user_form}) 

@login_required
def edit(request):
    if request.method =='POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                     data=request.POST,files=request.FILES)
        if user_form.is_valid() and   profile_form.is_valid():
             user_form.save()
             profile_form.save()
             messages.success(request,'Profile Updated Successfuly')
        else:
            messages.error(request,'Error in Updting you Profile')
    else:
      user_form = UserEditForm(instance=request.user)
      profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'edit.html',{'user_form':user_form,'profile_form':profile_form})

def appointment(request):
    if request.method == "POST":
        user = Booking()
        user.name= request.POST.get('fullname')
        id = user.order_id
        user.phone= request.POST.get('contactno')
        user.email= request.POST.get('email')
        user.pickupdate= request.POST.get('pickupdate')
        user.from_address= request.POST.get('from-location')
        user.to_address= request.POST.get('to-location')
        user.weight= request.POST.get('weight')
        user.price= request.POST.get('Price')
        user.save()
        return render(request, 'appointment.html',{
             'id':id,
             'fullname': request.POST.get('fullname'),
             'contactno':request.POST.get('contactno'),
             'email': request.POST.get('email'),
             'pickupdate':request.POST.get('pickupdate'),
             'from_location':request.POST.get('from-location'),
             'to_location':request.POST.get('to-location'),
             'weight': request.POST.get('weight'),
             'Price':request.POST.get('Price')})


    else:
        return render(request,'index.html', {})


def search(request):
    if request.method == 'POST':
        if request.POST.get('orderno'):
            all_orders = Booking.objects.all()
            a = request.POST.get('orderno')
            a = a.strip()

            for x in all_orders:
                if x.orderid == a:
                    customer['id']= a;
                    customer['from']=x.from_address
                    customer['To']=x.to_address
                    customer['weight']=x.weight
                    customer['price']=x.price

                    flag =1;
                else:
                    continue

            if flag==1:
               flag =0
               return render(request,'search.html',customer)
        
    
    return render(request,'search.html')

        