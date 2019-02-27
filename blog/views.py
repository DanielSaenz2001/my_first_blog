from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template import RequestContext
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.core.urlresolvers import reverse_lazy

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post" 

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {'titulo': 'Crear Post'}
        return super().get_context_data(**context, **kwargs)    

class PostEdit(UpdateView):
    model = Post
    form_class= PostForm
    success_url= reverse_lazy("post_list")
    def get_context_data(self, **kwargs):
        context = {'titulo': 'Editar Post'}
        return super().get_context_data(**context, **kwargs)

class PostRemove(DeleteView):
    model = Post
    success_url= reverse_lazy("post_list")
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class PostDraftList(ListView):
    model = Post
    template_name_suffix= "_draft_list"
    queryset= Post.objects.filter(published_date__isnull=True).order_by('create_date')

class PostPublish(View):
    model= Post
    success_url= reverse_lazy("post_list")
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(self.model, pk=kwargs.get('pk'))
        post.publish()
        return HttpResponseRedirect(self.success_url)

class CommentApprove(View):
    model= Comment
    success_url= reverse_lazy("post_list")
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(self.model, pk=kwargs.get('pk'))
        comment.approve()
        return HttpResponseRedirect(self.success_url)

class CommentRemove(View):
    model= Comment
    success_url= reverse_lazy("post_list")
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(self.model, pk=kwargs.get('pk'))
        comment.delete()
        return HttpResponseRedirect(self.success_url)

class AddCommentToPost(CreateView):
    model = Post
    form_class = CommentForm
    success_url = reverse_lazy("post_list")
    template_name_suffix= "_add_comment_to_post"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post= get_object_or_404(Post, pk=self.kwargs.get('pk'))
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)