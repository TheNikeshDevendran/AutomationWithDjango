from django.shortcuts import render

# Create your views here.
def importData(request):
    return render(request,'dataentry/importData.html')