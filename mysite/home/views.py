from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect


from .models import Quilt
from .forms import QuiltForm

def home(request):
    quilts = Quilt.objects.all()
    paginator = Paginator(quilts, 8)
    page = request.GET.get('page')
    try:
        quilt_list = paginator.page(page)
    except PageNotAnInteger:
        quilt_list = paginator.page(1)
    except EmptyPage:
        quilt_list = paginator.page(paginator.num_pages)
    template = 'home/index.html'
    return render(request, template, {'quilt_list': quilt_list})


def add(request):
    if request.method == 'POST':
        quiltform = QuiltForm(request.POST, request.FILES)
        instance = quiltform.save(commit=False)
        instance.cost = request.POST.get('cost')
        instance.quiltID = request.POST.get('name')
        instance.pic = request.FILES['uploadFromPC']
        instance.save()
        return HttpResponseRedirect('/home/home')
    else:
        quiltform = QuiltForm()

    template = 'home/add.html'
    return render (request, template)
