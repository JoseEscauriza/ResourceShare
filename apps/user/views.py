from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def user_list(request):
    users = User.objects.all()

    context = {"users": users}
    return render(request, "user/user_list.html", context)


def login_view(request):
    error_message = None

    # Unbound state of our form
    form = AuthenticationForm()

    if request.method == 'POST':
        # Bound state of our form
        form = AuthenticationForm(data=request.POST)

    # Validate the data
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # authenticate the user
        user = authenticate(
            username=username,
            password=password,
        )

        # Check if user was authenticated
        if user is not None:
            # use the session to keep the authenticated user's id
            login(request, user)
            # When we login, the session will store the user id
            # The authentication middleware is going to use that id
            # and fetch the user from the db and store it in the request.user object

            # redirect the user to his profile page
            # the url path name
            return redirect("profile")

        # TODO: If user is not authenticated, what do?

    else:
        # User data is not valid. Set an error message to be displayed
        error_message = "Sorry, something went wrong. Please try again"

    context = {'form': form, "error_message": error_message}

    return render(
        request,
        template_name="user/login.html",
        context=context
    )


def profile(request):
    return render(
        request,
        'user/profile.html'
    )
