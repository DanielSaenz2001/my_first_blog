from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/new', views.PostCreate.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/', views.PostEdit.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostRemove.as_view(), name='post_remove'),  
    url(r'^post/(?P<pk>\d+)/comment/$', views.AddCommentToPost.as_view(), name='add_comment_to_post'),    
    url(r'^drafts/', views.PostDraftList.as_view(), name='post_draft_list'),  
    url(r'^post/(?P<pk>\d+)/publish/', views.PostPublish.as_view(), name='post_publish'),    
    url(r'^comment/(?P<pk>\d+)/approve/$', views.CommentApprove.as_view(), name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.CommentRemove.as_view(), name='comment_remove'),
]