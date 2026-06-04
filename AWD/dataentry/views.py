from django.shortcuts import render
from . import utils
# Create your views here.
def importData(request):
    if request.method == "POST":
        return ''
    else:
        models=utils.get_all_custom_models()
        print(models)
    return render(request,'dataentry/importData.html')