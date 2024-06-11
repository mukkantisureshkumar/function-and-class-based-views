from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from app.forms import *
# Create your views here.
def string_by_fbv(request):
    return HttpResponse('<center><h1>String is returned by <u>Function Based View</u></h1></center>')

class string_by_cbv(View):
    def get(self,request):
        return HttpResponse('<center><h1>String is returned by <u>Class Based View</u></h1></center>')



def html_by_fbv(request):
    return render(request,'html_by_fbv.html')

class html_by_cbv(View):
    def get(self,request):
        return render(request,'html_by_cbv.html')



def insert_by_fbv(request):
    d={'k':SchoolForm()}
    if request.method=='POST':       
        collect=SchoolForm(request.POST)
        if collect.is_valid():
            collect.save()
            return HttpResponse("data inserted")
        else:
            return HttpResponse("not inserted")
    return render(request,'insert_by_fbv.html',d)

class insert_by_cbv(View):
    def get(self,request):
        scl=SchoolForm()
        d={'k':scl}
        return render(request,'insert_by_cbv.html',d)
    def post(self,request):
        collect=SchoolForm(request.POST)
        if collect.is_valid():
            collect.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data not inserted')


# to render only html page not context
class tem_plate(TemplateView):
    template_name='tem_plate.html'
