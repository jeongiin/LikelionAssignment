from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects    #쿼리셋 #메소드
    return render(request,'home.html',{'blogs':blogs})

# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소드

def detail(request, blog_id): #request 이외에 추가적인 정보(몇번 객체)필요.
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #데이터베이스에 저장.
    return redirect('/blog/'+str(blog.id)) #괄호안에 있는 url로 이동

