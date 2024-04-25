from django.shortcuts import render, get_object_or_404
from .models import PortfolioItem

# Create your views here.
def portfolio_list(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'items': items})


def portfolio_detail(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio_item': portfolio_item})
