from django.urls import path
from .views import(HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)

urlpatterns = [
    path(r'', HomePageView.as_view(), name = 'home'),
    path(r'articles', ArticleList.as_view(), name = 'articles_list'),
    path(r'articles/category/<slug:slug>/', ArticleCategoryList.as_view(), name = 'articles_category_list'),
    path(r'articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name = 'news_detail'),
]