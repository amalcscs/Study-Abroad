from django.shortcuts import render,redirect

# Create your views here.

def DocumentOfficer_index(request):
    return render(request,"DocumentOfficer_index.html")