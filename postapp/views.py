from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from sympy import re
from .models import *

def postlist(request):
    posts = Post.objects.all()
    return render(request, 'postapp/postlist.html', {'posts':posts})

def postlist_id(request, id):
    posts = Post.objects.filter(id=id)
    return render(request, 'postapp/postlist.html', {'posts':posts})

# show 함수를 실행할 때, path-converter(id) 를 인자로 받는다
# post 변수는 Post DB 에서 pk가 id 에 해당하는 객체를 가져온다.
# 해당하는 객체가 없을 경우 404 Error 출력
def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'postapp/show.html', {'post':post})

# CRUD
from .forms import PostForm


def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':    # post 방식으로 요청이 들어왔을 때
        form = PostForm(request.POST) # 입력된 내용들을 form 이라는 변수에 저장
        if form.is_valid():             # form 이 유효하다면
            post = form.save(commit=False) # form 데이터를 가져온다.
            post.save()                     # form 데이터를 DB에 저장한다.
            return redirect('postlist')
        else:
            return redirect('postlist')
    else:
        form = PostForm()
        return render(request, 'postapp/new.html', {'form':form})


def edit(request):
    return render(request, 'edit.html')

def postupdate(request, id):
    post = get_object_or_404(Post, pk=id)  # path-converter로 받은 id로 수정하고자 하는 post객체를 get
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post) # PostForm의 인스턴스는 post임을 표시
        if form.is_valid:
            post=form.save(commit=False)
            post.save()
            return redirect('show', id = post.pk)
        else:
            return redirect('postlist')
    else:
        form = PostForm(instance=post)   # get 으로 요청이 들어온 경우, post 에 기존에 입력되어있떤 내용을 form 에 담아서 edit.html 을 렌더링
        return render(request, 'postapp/edit.html',{'form':form})



