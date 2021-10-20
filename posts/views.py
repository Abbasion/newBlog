from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from posts.models import Posts,Gallery,PostsForm,Category
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.http import JsonResponse
from django.core.mail import send_mail, send_mass_mail, mail_admins, mail_managers

class index(FormView):
    template_name = "index.html"
    form_class = PostsForm
    success_url = '/'

class show(TemplateView):
    template_name = "list_posts.html"
    model = Posts
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['object_list']= self.model.objects.all()
        return context


class add(CreateView):
    # model = Posts
    # fields = '__all__'
    form_class = PostsForm
    template_name = 'posts/posts_form.html'
    success_url = '/'
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        files = self.request.FILES.getlist('thumbnail')
        response = super().form_valid(form)
        for f in files:
            gallery = Gallery(post_id=self.object.pk, images=f)
            gallery.save()
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'success': "Record Successfully Added",
            }
            return JsonResponse(data)
        else:
            return response

class edit(UpdateView):
    # model = Posts
    # fields = '__all__'
    form_class =PostsForm
    success_url = '/'

    def get_queryset(self):
        id = self.kwargs['pk']
        return Posts.objects.filter(pk=id)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        Gallery.objects.filter(post_id=self.kwargs['pk']).delete()
        files = self.request.FILES.getlist('thumbnail')
        response = super().form_valid(form)
        for f in files:
            gallery = Gallery(post_id=self.object.pk, images=f)
            gallery.save()
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'success': "Record Successfully Updated",
            }
            return JsonResponse(data)
        else:
            return response

class delete(DeleteView):
    model = Posts
    success_url = reverse_lazy('show')

def send_mails(request):
    mail_admins('Error i Found', 'we have found some errors', fail_silently=False)
    mail_managers('Error i Found', 'we have found some errors', fail_silently=False)
    return HttpResponse("Emails send to Admin")


    # Mass mailing Using send_mass_mail function

    # mail1 = ("Test Subject", "Hello, How are you? This is text",'admin@admin.com',['test@test.com'],
    # html_message="<h2>Hello, How are you? this is html</h2>")

    # mail2 = ("Test Subject", "Hello, How are you? This is text",'admin@admin.com',['test@test.com'],
    # html_message="<h2>Hello, How are you? this is html</h2>")

    # mail = send_mass_mail((mail1, mail2), fail_silently=False)
    # if mail:
    #     return HttpResponse(mail)
    # else:
    #     raise Exception("Error")

    # single mail using send_mail function

    # mail = send_mail("Test Subject", "Hello, How are you? This is text",'admin@admin.com',['test@test.com'],
    # fail_silently=False,html_message="<h2>Hello, How are you? this is html</h2>")

    # if mail:
    #     return HttpResponse(mail)
    # else:
    #     raise Exception("Error")

    # email send to the multiple people using send_mail function

    # mail1 = send_mail("Test Subject", "Hello, How are you? This is text",'admin@admin.com',['test@test.com'],
    # fail_silently=False,html_message="<h2>Hello, How are you? this is html</h2>")

    # mail2 = send_mail("Test Subject", "Hello, How are you? This is text",'admin@admin.com',['test@test.com'],
    # fail_silently=False,html_message="<h2>Hello, How are you? this is html</h2>")

    # if mail1 and mail2:
    #     return HttpResponse(mail)
    # else:
    #     raise Exception("Error")

   