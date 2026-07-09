from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login


from django.contrib.auth import get_user_model
User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect("index")

    return render(request,"users/login.html")




def register_view(request):
    if request.method=="POST":

        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password1"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request,"users/register.html")