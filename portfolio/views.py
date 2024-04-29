from django.shortcuts import render, get_object_or_404, redirect
from .models import PortfolioItem
from .forms import CommentForm

# Create your views here.
def portfolio_list(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'items': items})


def portfolio_detail(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.portfolio_item = portfolio_item
            comment.author = request.user
            comment.save()
            return redirect('portfolio_detail', pk=portfolio_item.pk)
    else:
        form = CommentForm()
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio_item': portfolio_item, 'form': form})
