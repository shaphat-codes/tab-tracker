
from django.contrib import admin
from django.urls import path
from tracker import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    path('new-tab-list', views.NewTabList, name ='new-tab-list'),
    path('new-tab-filter/', views.NewTabFilterView, name ='new-tab-filter'),
    path('new-tab-create', views.NewTabCreate, name ='new-tab'),
    path('switch-tab-create', views.SwitchTabCreate, name ='switch-tab'),
    path('switch-tab-list', views.SwitchTabList, name ='switch-tab-list'),

]
