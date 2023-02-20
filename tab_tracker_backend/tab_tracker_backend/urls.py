
from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new-tab-list', views.NewTabList, name ='new-tab-list'),
    path('new-tab-filter/', views.NewTabFilterView, name ='new-tab-filter'),
    path('new-tab-create', views.NewTabCreate, name ='new-tab'),
    path('switch-tab-create', views.SwitchTabCreate, name ='switch-tab'),
    path('switch-tab-list', views.SwitchTabList, name ='switch-tab-list'),

]
