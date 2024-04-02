import json



from multiprocessing import context
from typing import Any
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render,redirect
from django.template.response import TemplateResponse

from django.urls import reverse

from .models import Post
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt

from .forms import PostForm
from .post.models import Post


from .serializer import PostSerializer, PostCreateSerializer, PostListModelSerializer, PostListModelsSerializer
# Create your views here.

#def index(request):
    #print(request)
    #print(request.scheme)
    #print(request.path)
    #print(request.encoding)
   # return HttpResponse('<h1>Hello World!</h1>')

#def index_2(request):
   # return HttpResponse('<h1>Hello World! index_2</h1>')

#def about(request):
    #print('http://127.0.0.1:8000'+request.get_full_path())
   # return HttpResponse('<a href="#"> About page! </a>')

#def contacts(request):
   # print(request.path)
    #return HttpResponse('<h2> Contacts page </h2>')

#def ggg(request):
   # return HttpResponse('<h2> GGG page </h2>')

#def archive(request):
   # return HttpResponse('Archive page')

#def archive_2(request):
   # return HttpResponse('Archive page 2')

#def group(request):
   # group_number = request.path
   # return HttpResponse('group #{group_number}')

#def home_1(request):
   # header = 
   # return HttpResponse(page_content)

def posts(request):
    posts = Post.objects.all()
    data = {
        'title': 'All posts',
        'message': 'hello guys',
        'posts': posts,
    }
    return render(request, 'posts.html', context=data)

def post_detail(request, post_id):
    return HttpResponse(f'detail: {post_id}')

def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
        raise Http404
    return HttpResponse(f'archive for: {year}')

def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    return HttpResponse('GET request')

def template_test(request):
    return TemplateResponse(request, 'template_test.html')

def get_post_by_id(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {
        'id': post.id,
        'title': post.title_name,
        'content': post.content,
    }
    return JsonResponse(data)

#def delete_post(request,post_id=None):
   # post_to_delete=Post.objects.get(id=post_id)
    #post_to_delete.delete()
   # return HttpResponseRedirect(<h1> ALL posts deleted </h1>)
        
def error_404(request, exception):
    return HttpResponseNotFound('''
        <h3> Page not found :^(</h3>
        <img class='fit-picture' 
                                src="https://w.forfun.com/fetch/91/91ab23cdc35b6b44d15f1f5ebeb1cfdf.jpeg" 
                                alt='Imagination' />
    ''')

def page_404(request, exception):
    return HttpResponseNotFound('<h3>Page not found :^</h3>')

#def error_404(request, exception):
   #context = {}
   #return render(request,'admin/404.html', context)

def delete(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = get_object_or_404(self.model, pk=post_id)
        post.delete()
        return JsonResponse({'message': 'Post deleted successfully'}, status=156)

class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name ='post/list.html'
    context_object_name ='posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'p'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().def get_context_data(self, **kwargs) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context["form"] = PostForm()
            return context
        
class CreatePostView(CrateView):
    model = Post
    template_name = 'post/create.html'
    fields = ['title', 'user', 'status']

class AboutView(TemplateView):
    template_name = 'post/about.html'

def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
       # raise Http404
        return redirect('post_detail', 3)
    

    return HttpResponse(f'archive for: {year}')

@csrf_exempt
def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    is_active = request.GET.get('is_active')
    user = request.GET.get('user')

    posts = Post.objects.filter(is_active=bool(is_active), user__username=user)
    response = {
        'posts': list(posts)
    }
    return JsonResponse
    
class PostAPIView(APIView):
    
    def get(self, request):
        post_queryset = Post.objects.all()
        serialixer = PostListSerialixer(post_queryset, many=True)
        return Response(serializer.data)
    
    def get(self, request):
        serialixer = PostCreateSerilizer(data=request.data)
        serialixer.is_valid()

        user = User.objects.get(id=serializer.validated_data.pop('user'))
        categorories = serializer.validated_data.pop('categories')
        print(serializer.validated_data)
        post=Post.objects.create(user=user, **serialixer.validated_data)
        post.categories.add(*catigories)

        return Response('created!!')
    