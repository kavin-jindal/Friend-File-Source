from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from kavinblog.models import Profile, Post
from django.http import Http404


# Create your views here.

class CreateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = "registration/create_profile.html"
	#fields = '__all__'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)



class EditProfilePageView(UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'


  
class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context

class UserRegisterView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  #fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'bio', 'profile_pic']
  success_url = reverse_lazy('login')
  


class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('password_success')


def password_success(request):
	return render(request, 'registration/password_success.html', {})

