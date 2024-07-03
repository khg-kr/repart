from django.shortcuts import render
from .models import Part
from django.core.paginator import Paginator
from django.db.models import Q


def part_list(request):

    query = request.GET.get('q')
    parts = Part.objects.none()
    message = ""

    if query:
        if len(query) >= 2:
            parts = Part.objects.filter(
#Q(category_code__icontains=query) |
                Q(part_code__icontains=query) |
                Q(part_name__icontains=query)
#            Q(part_price__icontains=query)
        )
    else:
        parts = Part.objects.all()

    paginator = Paginator(parts, 14)  # 페이지당 15개씩 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'part_list.html', {'page_obj': page_obj, 'query': query})

# Create your views here.
