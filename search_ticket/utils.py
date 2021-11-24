from .models import *
from django.contrib import messages


class DataMixin(object):

    """Mixin for all clases that we have to
    make they shorter and fater"""
    paginate_by = 10   #needs to be queryset in function(not import tegs '{% load menu_tags %}' )  

    def get_user_context(self, **kwargs):
        context = kwargs

        return context

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form) 
      
