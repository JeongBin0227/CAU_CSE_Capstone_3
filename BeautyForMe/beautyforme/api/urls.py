from django.conf.urls import url
from rest_framework.authtoken import views as token_views

from api import views

urlpatterns = [
    url(r'^user/cosmetic/importance/$', views.CosmeticImportanceInfo.as_view()),
    url(r'^user/cosmetic/importance/(?P<pk>[\w:|-]+)/$', views.CosmeticImportanceInfo.as_view()),
    url(r'^user/cosmetic/interested/$', views.UserInterestedCosmeticInfo.as_view()),
    url(r'^user/cosmetic/interested/(?P<pk>[\w:|-]+)/$', views.UserInterestedCosmeticInfo.as_view()),
    url(r'^user/cosmetic/$', views.UserCosmeticInfo.as_view()),
    url(r'^user/cosmetic/(?P<pk>[\w:|-]+)/$', views.UserCosmeticInfo.as_view()),
    url(r'^user/$', views.UserInfo.as_view()),
    url(r'^user/(?P<pk>[\w:|-]+)/$', views.UserInfo.as_view()),
    url(r'^profile/$', views.ProfileInfo.as_view()),
    url(r'^profile/(?P<pk>[\w:|-]+)/$', views.ProfileInfo.as_view()),
    url(r'^cosmetic/bigcategory/$', views.BigCategoryInfo.as_view()),
    url(r'^cosmetic/bigcategory/(?P<pk>[\w:|-]+)/$', views.BigCategoryInfo.as_view()),
    url(r'^cosmetic/smallcategory/$', views.SmallCategoryInfo.as_view()),
    url(r'^cosmetic/smallcategory/(?P<pk>[\w:|-]+)/$', views.SmallCategoryInfo.as_view()),
    url(r'^cosmetic/similar/$', views.SimilarCosmeticInfo.as_view()),
    url(r'^cosmetic/similar/(?P<pk>[\w:|-]+)/$', views.SimilarCosmeticInfo.as_view()),
    url(r'^cosmetic/$', views.CosmeticInfo.as_view()),
    url(r'^cosmetic/(?P<pk>[\w:|-]+)/$', views.CosmeticInfo.as_view()),
    url(r'^video/detail/$', views.VideoDetailInfo.as_view()),
    url(r'^video/detail/(?P<pk>[\w:|-]+)/$', views.VideoDetailInfo.as_view()),
    url(r'^video/filter/$', views.FilteredVideoInfo.as_view()),
    url(r'^video/filter/(?P<pk>[\w:|-]+)/$', views.FilteredVideoInfo.as_view()),
    url(r'^video/bookmark/$', views.VideoBookmarkInfo.as_view()),
    url(r'^video/bookmark/(?P<pk>[\w:|-]+)/$', views.VideoBookmarkInfo.as_view()),
    url(r'^video/$', views.AllVideoInfo.as_view()),
    url(r'^video/(?P<pk>[\w:|-]+)/$', views.AllVideoInfo.as_view()),
]