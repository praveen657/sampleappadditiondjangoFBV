from django.shortcuts import render

# Create your views here.
def addition(request):
	a = 3
	b = 2
	res = a + b
	return render(request,'sampleapp/add.html',{'result' : res})
