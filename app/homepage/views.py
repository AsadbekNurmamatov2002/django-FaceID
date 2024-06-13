from django.shortcuts import render

# Create your views here.


def HomePage(request):
    # print(request.user.get_full_name)
    return render(request, "home.html", {})