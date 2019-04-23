from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    # 使用django自带的views
    # 主页
    path('', views.IndexView.as_view(), name='index'),

    # 详情页
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # 投票的结果页
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # 使用自定义的views，投票页
    path('<int:question_id>/vote/', views.vote, name='vote'),
]