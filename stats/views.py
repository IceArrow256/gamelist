from django.shortcuts import render

import django.http as DH
import stats.utils as SU

def home(request):
    context = SU.get_context(request)
    return render(request, 'stats/home.html', context)