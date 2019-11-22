from django.shortcuts import render
from .models import Laptop
from django.core.paginator import Paginator
# Create your views here.
def index(request):
 
    return render(request, 'laptops/index.html')
    


# GET 요청을 받음
def search(request):
    # 1. request로부터 검색어 가져오기
    query = request.GET.get('query') #=> 'asdf'
    # 2. Article에서 제목에 검색어가 있는지 찾기
    laptops = Laptop.objects.filter(spec__contains = query)
    # 3. context로 결과값 template에 넘겨주기
    context = {
        'laptops' : laptops,
    }
    return render(request, 'laptops/search.html', context)