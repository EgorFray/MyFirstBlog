from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'bloggg/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'bloggg/post_detail.html'


class PostCreate(ObjectDetailMixin, View):
    model_form = PostForm
    template = 'bloggg/post_create_form.html'


class PostUpdate(View):
    model = Post
    model_form = PostForm
    template = 'bloggg/post_update_form.html'

    def get(self, request, slug):
        obj = Post.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        print(bound_form.errors)
        print('я ебал этот ваш дебагер')
        print(bound_form.is_valid())

        if bound_form.is_valid():
            new_obj = bound_form.save()
            print(bound_form.errors)
            print('я ебал этот ваш дебагер')
            return redirect(new_obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower(): obj})



class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'bloggg/tag_detail.html'


class TagCreate(ObjectDetailMixin, View):
    model_form = TagForm
    template = 'bloggg/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'bloggg/tag_update_form.html'

    #def get(self, request, slug):
    #    tag = Tag.objects.get(slug__iexact=slug)
    #    bound_form = TagForm(instance=tag)
    #    return render(request, 'bloggg/tag_update_form.html', context={'form':bound_form, 'tag':tag })

 #   def post(self, request, slug):
  #      tag = Tag.objects.get(slug__iexact=slug)
  #      bound_form = TagForm(request.POST, instance=tag)

   #     if bound_form.is_valid():
   #         new_tag = bound_form.save()
    #        return redirect(new_tag)
   #     return render(request, 'bloggg/tag_update_form', context={'form':bound_form, 'tag':tag })


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'bloggg/tags_list.html', context={'tags': tags})

