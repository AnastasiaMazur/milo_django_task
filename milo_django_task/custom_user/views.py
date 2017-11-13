import csv
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm


class UsersListView(ListView):
    queryset = User.objects.all()
    template_name = 'users.html'


class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'user_detail.html'

    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        obj = get_object_or_404(User, username=username)
        return obj


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = "/users/"

    def form_valid(self, form):
        form.save(commit=False)
        return super(UserCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(UserCreateView, self).get_context_data(*args, **kwargs)
        return context


class UserUpdateView(UpdateView):
    form_class = UserForm
    template_name = 'edit_user.html'
    success_url = "/users/"

    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        obj = get_object_or_404(User, username=username)
        return obj


class UserDeleteView(DeleteView):
    form_class = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('users')

    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        obj = get_object_or_404(User, username=username)
        return obj


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Number'])

    users = User.objects.all().values_list('username', 'birthday', 'number')
    for user in users:
        writer.writerow(user)

    return response



