from django.shortcuts import render
from django.views.generic.list import ListView
from .forms import SearchRouteForm
# Create your views here.


def search_ticket(request):
    form = SearchRouteForm()
    if request.method == 'POST':
        form = SearchRouteForm(request, request.POST)
        try:
            if form.is_valid():
               pass 
               
                
        except TypeError:
            # messages.add_message(request, messages.ERROR,
            #                 ' Wrong username or password')          
            pass  
    else:
        form = SearchRouteForm()
    return render(request, 'icon/sign_in.html', {'form': form})
 