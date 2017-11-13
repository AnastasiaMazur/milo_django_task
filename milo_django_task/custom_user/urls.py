from django.conf.urls import url
from custom_user import views
from .views import UsersListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    url(r'^users/$', UsersListView.as_view(), name='users'),
    url(r'^users/create/$', UserCreateView.as_view(), name='add_user'),
    url(r'^users/(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='user'),
    url(r'^users/(?P<username>[\w.@+-]+)/edit/$', UserUpdateView.as_view(), name='edit_user'),
    url(r'^users/(?P<username>[\w.@+-]+)/delete/$', UserDeleteView.as_view(), name='delete_user'),
    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
    url(r'^', UsersListView.as_view(), name='home'),
]
