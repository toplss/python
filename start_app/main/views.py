from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Test

# Create your views here.
def index(request):
    return render(request,'main/index.html')


# blog.html 페이지를 부르는 blog 함수
def blog(request):
    postlist = Test.objects.all().order_by('-id')
    paginator = Paginator(postlist, 10) # 10개의 데이터를 보여줍니다.
    page = request.GET.get('page') # 현재 페이지 번호를 가져옵니다.

    try:
        postlist = paginator.get_page(page)
    except PageNotAnInteger: # 페이지 번호가 정수가 아닌 경우
        postlist = paginator.get_page(1) # 첫 페이지를 보여줍니다.
    except EmptyPage: # 페이지 번호가 유효하지 않은 경우
        postlist = paginator.get_page(paginator.num_pages) # 마지막 페이지를 보여줍니다.


    return render(request,'main/blog.html', {'postlist' : postlist})


def write(request):
    return render(request,'main/write.html')


def blog_register(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('content')
        # POST 데이터를 처리하는 코드 작성
        b = Test(
            title = title,
            contents = contents
        )
        b.save()

        return redirect('blog')
    else:
        return redirect('blog')


