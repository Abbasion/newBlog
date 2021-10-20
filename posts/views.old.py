# from django.shortcuts import render, redirect
# from posts.models import Posts,Gallery,PostsForm,Category
# from django.views.generic import TemplateView,ListView,View
# # Create your views here.
# def index(request):
#     form = PostsForm()
#     data = Posts.objects.all()
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         form = PostsForm(request.POST, request.FILES)
#         files = request.FILES.getlist('thumbnail')
#         if form.is_valid():
#             post = form.save(commit=False)
#             form.save()
#             for f in files:
#                 gallery = Gallery(post=post, images=f)
#                 gallery.save()
#             return redirect('/')
#     return render(request, 'index.html', {'title': 'Add New Post', 'form': form, 'rows': data, 'categories': categories})
#
# class cbview(TemplateView):
#     template_name = 'class_view.html'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(cbview, self).get_context_data(**kwargs)
#         # context["object_list"]=Posts.objects.all
#         context = {
#             'object_list': Posts.objects.all(),
#             'form': PostsForm()
#         }
#         return context
#     # def get(self,request):
#     #     data = Posts.objects.all()
#     #     form = PostsForm()
#     #     return render(request, self.template_name, {'object_list': data, 'form': form})
#
#     def post(self,request):
#         form = PostsForm()
#         data = Posts.objects.all()
#         categories = Category.objects.all()
#         if request.method == 'POST':
#             form = PostsForm(request.POST, request.FILES)
#             files = request.FILES.getlist('thumbnail')
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 form.save()
#                 for f in files:
#                     gallery = Gallery(post=post, images=f)
#                     gallery.save()
#                 return redirect(self.template_name  )