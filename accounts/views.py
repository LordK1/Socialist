from allauth.account.forms import LoginForm

from allauth.account.views import SignupView, LoginView
from braces.views import LoginRequiredMixin, AjaxResponseMixin, JsonRequestResponseMixin
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect, JsonResponse
from django.views.generic import FormView, DetailView
from django.views.generic.base import TemplateView, RedirectView

from accounts.forms import RegistrationForm, ContactForm, MyLoginForm
from accounts.models import Author


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'


class RegistrationView(FormView):
    template_name = 'accounts/signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        saved_user = form.save()
        user = authenticate(username=saved_user.username, password=form.cleaned_data['password1'])
        login(request=self.request, user=user)
        return HttpResponseRedirect(self.get_success_url())


class MySignUpView(SignupView):
    template_name = "accounts/signup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super(MySignUpView, self).get_context_data(**kwargs)
        context['all_tags'] = "Tags are responsed !!!"
        context['message'] = self.request.user + " Welcome to Socialist !!!"
        return context


class MyLoginView(LoginView):
    """
    if you want to use LoginForm of django-allauth
    you should resolve all dependencies on templates and urls !
    """
    template_name = 'accounts/login.html'
    form_class = MyLoginForm
    success_url = reverse_lazy('dashboard')

    def __init__(self, **kwargs):
        super(MyLoginView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(MyLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super(MyLoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyLoginView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(MyLoginView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['message'] = self.request.user.username + " Welcome to Socialist !!! "
        return context


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request=request)
        return super(LogoutView, self).get(request, args, kwargs)


class PasswordRecoveryView(FormView):
    pass


class SettingsView(FormView):
    pass


class SubscribeView(AjaxResponseMixin, FormView, JsonRequestResponseMixin):
    template_name = 'home.html'
    success_url = reverse_lazy('home')
    form_class = ContactForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if self.request.is_ajax():
            # print('Email : ' + email)
            data = {
                'result': email,
                'message': 'success'
            }
            return JsonResponse(data)


class AuthorDetailView(DetailView, LoginRequiredMixin):
    model = Author
    template_name = 'accounts/author_detail.html'
    login_url = settings.LOGIN_REDIRECT_URL
    context_object_name = 'author'
