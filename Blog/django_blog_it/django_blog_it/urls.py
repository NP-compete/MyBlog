from django.conf.urls import url
from .views import *
from django_blog_it.posts.views import *
from recognition.views import UserLoginView, LogoutView

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    #url(r'^$', AdminLoginView.as_view(), name='admin_login'),
    url(r'^$', UserLoginView.as_view(), name='login'),
    #url(r'^logout/$', admin_logout, name='admin_logout'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', PostList.as_view(), name='blog'),
    #url(r'^add/$', PostCreateView.as_view(), name='blog_add'),
    #url(r'^view/(?P<blog_slug>[-\w]+)/$', PostDetailView.as_view(), name='view_blog'),
    #url(r'^delete/(?P<blog_slug>[-\w]+)/$', PostDeleteView.as_view(), name='delete_blog'),
    #url(r'^edit/(?P<blog_slug>[-\w]+)/$', PostEditView.as_view(), name='edit_blog'),
    #url(r'^add_category/$', CategoryCreateView.as_view(), name='add_category'),
    #url(r'^category/$', CategoryList.as_view(), name='categories'),
    #url(r'^delete_category/(?P<category_slug>[-\w]+)/$', CategoryDeleteView.as_view(), name='delete_category'),
    #url(r'^edit_category/(?P<category_slug>[-\w]+)/$', CategoryUpdateView.as_view(), name='edit_category'),

    url(r'^bulk_actions_menu/$', MenuBulkActionsView.as_view(), name='bulk_actions_menu'),
    url(r'^bulk_actions_blog/$', BlogPostBulkActionsView.as_view(), name='bulk_actions_blog'),
    url(r'^bulk_actions_category/$', CategoryBulkActionsView.as_view(), name='bulk_actions_category'),
    url(r'upload_photos/$', upload_photos, name='upload_photos'),
    url(r'recent_photos/$', recent_photos, name='recent_photos'),

    # menu management
    #url(r'^menu/$', MenuListView.as_view(), name='menus'),
]
