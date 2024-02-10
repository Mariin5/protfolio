from django.shortcuts import render
from django.views import View
from .models import Category,Area,Photo


def home(request):
    photos = Photo.objects.all()
    return render(request,'home.html',{'photos':photos})

class CategoryList(View):
        #template_name = 'templates/home.html'
        model = Category

        def get(self, request, *args, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
detail = CategoryList.as_view()

class AreaList(View):
        #template_name = 'templates/home.html'
        model = Area

        def get(self, request, *args, **kwargs):
            context = {}
            return context
detail = AreaList.as_view()

class PhotoDetailView(View):

    def get(self, request, pk, *args, **kwargs):

        context = {}
        context["photo"]   = Photo.objects.filter(id=pk).first()

        return render(request, "photo_detail.html", context)

photo_detail   = PhotoDetailView.as_view()

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")