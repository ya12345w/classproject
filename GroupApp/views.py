from django.shortcuts import render

# Create your views here.
def ContactsView(request):
    return render(request,"ContactsView.html")
def HeadView(request):
    return render(request,"head.html")

