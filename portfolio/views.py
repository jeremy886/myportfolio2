from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('portfolio_list')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def portfolio_likes(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk)
    if request.user in portfolio_item.likes.all():
        portfolio_item.likes.remove(request.user)
    else:
        portfolio_item.likes.add(request.user)
    return HttpResponseRedirect(reverse('portfolio_detail', args=[str(pk)]))
