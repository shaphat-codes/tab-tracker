from . models import *
import django_filters

class NewTabFilter(django_filters.FilterSet):
    class Meta:
        model = NewTab
        fields = ['url']