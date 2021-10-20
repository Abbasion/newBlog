from django.core.serializers import serialize
from posts.models import Posts, PostsForm
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def users(requestm, pk=None):
    if request.method == "POST":
        post = PostsForm(request.POST, request.FILES)
        if (post.is_valid()):
            post.save()
            post = {
                'message': 'Form Submitted Successfully!',
                'id' : post.pk
            }
        else:
            post = {
                'message': 'There is Error in Your Form',
                'error': post.errors.get_json_data()
            }
        posts = json.dumps(post)
    else:
        if pk is None:
            posts = Posts.objects.all()
        else:
            posts = Posts.objects.filter(pk=pk)
        posts = serialize('json', posts, fields=('title', 'thumbnail','content', 'created_at', 'user', 'category'),
        use_natural_foreign_keys=True)

    return HttpResponse(posts, content_type="application/json")

    # if pk is None:
    #     posts = Posts.objects.all()
    # else:
    #     posts = Posts.objects.filter(pk=pk)

    # posts = serialize('json', posts, fields=('title', 'thumbnail','content', 'created_at', 'user', 'category'),
    # use_natural_foreign_keys=True)