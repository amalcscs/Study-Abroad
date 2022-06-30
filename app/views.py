from django.shortcuts import render,redirect

# Create your views here.

def DocumentOfficer_index(request):
    return render(request,"DocumentOfficer_index.html")
    
def DocumentOfficer_dashboard(request):
    return render(request,"DocumentOfficer_dashboard.html")
    
def DocumentOfficer_CurrentLeads_table(request):
    return render(request,"DocumentOfficer_CurrentLeads_table.html")