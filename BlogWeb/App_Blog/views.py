from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, UpdateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import HttpResponseRedirect
from .models import Blog,Likes
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.


class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'App_Blog/blog_list.html'

@login_required
def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = CommentForm()
    already_liked = Likes.objects.filter(user=request.user,blog=blog)
    if already_liked:
        like = True
    else:
        like = False

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            user_comment = form.save(commit=False)
            user_comment.user = request.user
            user_comment.blog = blog
            user_comment.save()

            return HttpResponseRedirect(reverse('App_Blog:blog_detail', kwargs={'slug':blog.slug}))

    dict={'form':form, 'blog':blog, 'like':like}

    return render(request, 'App_Blog/blog_detail.html', dict)

# class BlogDetail(LoginRequiredMixin,DetailView,CreateView):
#     model = Blog,Comment
#     # context_object_name = 'blog'
#     fields = ('blog_comment', )
#     template_name = 'App_blog/blog_detail.html'

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ['blog_title','blog_content','blog_image']
    template_name = 'App_Blog/update_blog.html'

    def get_success_url(self):
       return reverse_lazy('App_Blog:my_blog')

class MyBlog(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'App_Blog/my_blog.html'

class BlogWrite(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ['blog_title','blog_content','blog_image']
    template_name = 'App_Blog/blog_write.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.user = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','+') + '+' + str(uuid.uuid4())
        blog_obj.save()

        return HttpResponseRedirect(reverse('App_Blog:my_blog'))

@login_required
def liked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user

    already_liked = Likes.objects.filter(user=user,blog=blog)
    if not already_liked:
        liked = Likes(user=user,blog=blog)
        liked.save()

    return HttpResponseRedirect(reverse('App_Blog:blog_detail', kwargs={'slug':blog.slug}))

@login_required
def unliked(request,pk): 
    blog = Blog.objects.get(pk=pk)
    user = request.user

    already_liked = Likes.objects.filter(user=user,blog=blog)
    if already_liked:
        already_liked.delete()
    
    return HttpResponseRedirect(reverse('App_Blog:blog_detail', kwargs={'slug':blog.slug}))