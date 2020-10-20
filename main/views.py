from django.shortcuts import render
from .models import Numbering
from django.db.models import Q
from django.views.generic import View


def tels_list(request):
    """В виде процедуры"""
    search_query = request.GET.get('search', '')
    search_kod = search_query[2:5]
    search_nom = search_query[7:10] + search_query[11:15]

    tels = None
    if search_query:
        tels = Numbering.objects.filter(Q(kod__icontains=search_kod) &
                                        Q(fr__lt=int(search_nom)) &
                                        Q(to__gt=int(search_nom)))

    context = {'tels': tels, 'search_kod': search_kod, 'search_nom': search_nom}
    return render(request, 'main/index.html', context=context)


class Search(View):
    """В виде класса"""
    template = 'main/index.html'

    def get(self, request):
        search_query = request.GET.get('search', '')
        search_kod = search_query[2:5]
        search_nom = search_query[7:10] + search_query[11:15]

        tels = None
        if search_query:
            tels = Numbering.objects.filter(Q(kod__icontains=search_kod) &
                                            Q(fr__lt=int(search_nom)) &
                                            Q(to__gt=int(search_nom)))

        context = {'tels': tels, 'search_kod': search_kod, 'search_nom': search_nom}
        return render(request, self.template, context=context)

