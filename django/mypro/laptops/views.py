from django.shortcuts import render
from .models import Laptop
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    laptop_list = Laptop.objects.all()

    # Pagination
    # 1. arrticles를 Paginator에 입력
    paginator = Paginator(laptop_list,20)
    # 2. 몇번째 page를 보여줄건지 GET으로 가져옴
    page = request.GET.get('page')
    # 3. 해당하는 page의 articles만 뽑기
    laptops = paginator.get_page(page)
    
    context = {
        'laptops' : laptops,
    }

    return render(request, 'laptops/index.html', context)
    


def search(request):
    return render(request, 'laptops/search.html')