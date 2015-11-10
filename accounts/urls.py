from django.conf.urls import url, include

from accounts.views import SettingsView, PasswordRecoveryView, LogoutView, DashboardView, \
    SubscribeView, MySignUpView, MyLoginView, AuthorDetailView

urlpatterns = [
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^signup/$', MySignUpView.as_view(), name='signup'),
    url(r'^login/$', MyLoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^password_recovery/$', PasswordRecoveryView.as_view(), name='password_recovery'),
    url(r'^settings/$', SettingsView.as_view(), name='settings'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author'),
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),
    url(r'', include('allauth.urls')),
]
