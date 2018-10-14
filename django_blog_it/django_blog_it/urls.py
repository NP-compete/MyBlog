from django.conf.urls import url
from .views import admin_login, admin_logout, PostList, PostCreatView, PostDetailView, PostDeleteView, edit_blog, add_category, categories, delete_category, edit_category, bulk_actions_menu, bulk_actions_blog, bulk_actions_category, upload_photos, recent_photos, menus

urlpatterns = [
    url('', admin_login, name='admin_login'),
    url('logout/', admin_logout, name='admin_logout'),
    url('blog/', PostList.as_view(), name='blog'),
    url('add/', PostCreatView.as_view(), name='blog_add'),
    url('view/(?P<blog_slug>[-\w]+)/', PostDetailView.as_view(), name='view_blog'),
    url('delete/(?P<blog_slug>[-\w]+)/', PostDeleteView.as_view(), name='delete_blog'),
    url('edit/(?P<blog_slug>[-\w]+)/', edit_blog, name='edit_blog'),
    url('add_category/', add_category, name='add_category'),
    url('category/', categories, name='categories'),
    url('delete_category/(?P<category_slug>[-\w]+)/', delete_category, name='delete_category'),
    url('edit_category/(?P<category_slug>[-\w]+)/', edit_category, name='edit_category'),

    url('bulk_actions_menu/', bulk_actions_menu, name='bulk_actions_menu'),
    url('bulk_actions_blog/', bulk_actions_blog, name='bulk_actions_blog'),
    url('bulk_actions_category/', bulk_actions_category, name='bulk_actions_category'),
    url('upload_photos/', upload_photos, name='upload_photos'),
    url('recent_photos/', recent_photos, name='recent_photos'),

    # menu management
    url('menu/', menus, name='menus'),
]
