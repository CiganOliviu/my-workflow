from django.shortcuts import render


def index(request):
    template = 'views/index.html'

    return render(request, template_name=template)

