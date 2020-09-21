from django.shortcuts import render
from contents.models import Content
# Create your views here.


def list_contents(request):
    qs= Content.objects.all()
    context = {'contents_list':qs}
    return render(request, 'contents/listContents.html',context=context)
