from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_aluno/', views.get_aluno, name='get_aluno'),
    url(r'^generate_data/', views.generate_data, name='generate_data')
]
