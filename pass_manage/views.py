from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import PasswordEntry


# Create your views here.
def upload(request):
    if request.method == "POST":
        website_name = request.POST["web_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        note = request.POST["note"]

        PasswordEntry.objects.create(
            user=request.user,
            website_name=website_name,
            email=email,
            password=password,
            note=note
        )
        messages.success(request, "successfully uploaded")
        return redirect("home")

    return render(request, "upload.html")


def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        display_msg = None
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request, "username already taken")
                # return redirect("/login/sign-up")
                display_msg = "username already exists"
            elif User.objects.filter(email=email).exists():
                # messages.error(request, "email already taken")
                # return redirect("login/sign-up/")
                display_msg = "email already exists"
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                user.save()
                # messages.info(request, "successfully sign-in")
                # return redirect("/login")
                display_msg = "successfully created"
                return redirect('/login')
        
        else:
            # messages.error(request, "password miss match")
            # return redirect("/login/sign-up")
            display_msg = "Password did't match"
        msg = {"mess":display_msg}
        return render(request, "register.html", msg)
    else:
        return render(request, 'register.html')

def login(request):
    display_mes = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            # messages.info(request, 'Invalid details')
            # return redirect("/login")
            display_mes = "Invalid details"
            mess = {"mess":display_mes}
            return render(request, 'login.html', mess)


    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def my_account(request):
    return render(request, 'myaccount.html')

def getDetails(request):
    if request.method == "POST":
        web_name = request.POST.get("web_name")

        # Ensure the user is authenticated and logged in
        if request.user.is_authenticated:
            try:
                # Fetch credentials for the website name and logged-in user
                credentials = PasswordEntry.objects.get(website_name=web_name, user=request.user)
            except PasswordEntry.DoesNotExist:
                credentials = None
        else:
            credentials = None  # Handle case when user is not logged in

        return render(request, "findpasswords.html", {"credentials": credentials})

    return render(request, "findpasswords.html")

    
        