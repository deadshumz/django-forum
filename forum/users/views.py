from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import SignUpForm, SignInForm
from django.views import generic
from .models import Profile
from django.shortcuts import render, redirect

# Create your views here.
def auth_user(request,username,password):
    user = authenticate(username=username, password=password)
    login(request, user)

# Registration View
class RegistrationView(generic.edit.CreateView):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('main:index')
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        auth_user(self.request, form.cleaned_data['username'], form.cleaned_data['password2'])
        return redirect('main:index')

# SignIn View
class SignInView(generic.edit.FormView):
    template_name = 'users/signin.html'
    success_url = reverse_lazy('main:index')
    form_class = SignInForm

    def form_valid(self, form):
        auth_user(self.request, form.cleaned_data['username'], form.cleaned_data['password'])
        return redirect('main:index')

class UserProfileView(generic.detail.DetailView):
    model = Profile
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_profile = get_object_or_404(Profile, slug=self.kwargs['slug'])
        except KeyError:
            user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = {
            "target" : user_profile
            }
        return context

    def post(self, request, slug):
        user = Profile.objects.get(slug=slug)
        user.bio = request.POST['status']
        user.save()
        return HttpResponse(status=204)
