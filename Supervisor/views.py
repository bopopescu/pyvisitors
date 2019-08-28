from django.shortcuts import render

# Create your views here.
def view(request):
  return render(request,'supervisor_master.html')

def addVendar(request):
	return render(request,'Vendar/addVendar.html')

def viewVendar(request):
	return render(request,'Vendar/viewVendar.html')