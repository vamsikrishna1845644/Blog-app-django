from django.shortcuts import render,redirect
# redict function for redirecting
# there are inbuilt forms in django
from django.contrib.auth.forms import UserCreationForm
# we can add flash messages to tell the user that data is recide or crrect
from django.contrib import messages
# there are different types of messgaes which we can dissplay
# these messages will apear in our template for a short time until the next request is performed
#differnt types of messages are
"""
messages.debug
messages.success
messages.info
messages.warning
messages.error
"""
#now lets users our own created form from forms.py 
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# import a decaorator to keep users from accessing profile page without login
from django.contrib.auth.decorators import login_required

def register(request):
    #this is the place where logic lies about what happens when user submits his data 
    #u already know about http responses
    if request.method == 'POST':
        # gets data entered into forn variable
        form = UserRegisterForm(request.POST)
        #.is_valid() method checks if the user pressed sign up 
        if form.is_valid():
            #save the form
            form.save()
            # if yes then we can now get his username
            #.cleaned_data converts data in the form variable into a python dictionary on  which we can retrive desrieds fields
            username = form.cleaned_data.get('username')
            messages.success(request,f'account has bee created for {username}')
            return redirect('login')

    else:
        form = UserRegisterForm()
    
    #pass the form instance as context into render function
    #we also need to create the html template -register
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated succesfully')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context=context)
