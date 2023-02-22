from django.shortcuts import render
from django.shortcuts import redirect
from .models import Test

# Create your views here.
def index(request):
    return render(request,'main/index.html')


# blog.html 페이지를 부르는 blog 함수
def blog(request):
    postlist = Test.objects.all()
    print(postlist)
    return render(request,'main/blog.html', {'postlist' : postlist})


def blog_register(request):
    b = Test(title='test', contents='All the latest Beatles news.')
    b.save()

    return redirect('blog')
