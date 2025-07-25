from django.shortcuts import render
from django.http import HttpResponse

def portfolio_home(request):
    """Render the portfolio website"""
    return render(request, 'mypage.html')