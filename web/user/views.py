from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from . models import registration

# Create your views here.
def register(request):
    if  request.method =="POST":
        f_name = request.POST['First_name']
        m_name = request.POST['Middle_name']
        l_name = request.POST['Last_name']
        u_name = request.POST['Username']
        pass1 = request.POST['Password1']
        pass2 = request.POST['Password2']
        email = request.POST['Email']
        contact = request.POST['Contact']

        if (pass1 != pass2):
            messages.info(request, 'PASSWORD MISMATCHED!')
            return redirect('register')
        elif(User.objects.filter(username=u_name).exists()):
            messages.info(request, 'Username already taken!')
            return redirect('register')
        elif(User.objects.filter(email=email).exists()):
            messages.info.filter(request, 'Email already taken!')
            return redirect('register')
        else:
            user1 = registration(First_Name=f_name, Middle_Name=m_name, Last_Name=l_name, Username=u_name, Password=pass1, Email=email, Contact=contact)
            user = User.objects.create_user(Username=u_name, First_name=f_name, Last_name=l_name,Password=pass2, email=email)
            user1.save()
            user.save()
            return redirect('/user/login')

    else:
         return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        u_name = request.POST['username']
        pass1 = request.POST['password']
        user = auth.autheneticate(username = u_name, password = pass1)
        if user is not None:
            auth.login(request, user)
            return redirect ('/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('login')
    else:
        return render (request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect ('/')    
    



