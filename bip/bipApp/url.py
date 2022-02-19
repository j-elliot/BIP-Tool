from django.conf.urls import include, url
from django.urls import path
from bipApp.views import index, hello, viewArticle, viewArticles, ItemAutocomplete
import bipApp.views as views

app_name = 'bipApp'

urlpatterns = [

    path('', views.index, name='index'),
    url(r'^listicle/', views.ListicleView.as_view(), name='listicle'),
    path('project/<int:pk>/', views.ProjectView.as_view(), name='project'),
    path('task/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('report/<int:pk>/', views.ReportView.as_view(), name='report'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    url(r'^hello/', hello, name = 'hello'),
    url(r'^article/(\d+)/', viewArticle, name = 'article'),
    url(r'^articles/(\d{2})/(\d{4})', viewArticles, name = 'articles'),
    url(
        'item-autocomplete/$',
        ItemAutocomplete.as_view(),
        name='item-autocomplete',
    ),
]
