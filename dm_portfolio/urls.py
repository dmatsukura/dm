"""dm_portfolio app URL Configuration
"""
from django.urls import path
from dm_portfolio import dm_portfolio

app_name = "dm_portfolio"

urlpatterns = [
	path('portfolio/', dm_portfolio.PortfolioView.as_view, name="portfolios"),
	path('portfolio/<slug:slug>', dm_portfolio.PortfolioDetailView.as_view(), name="portfolio"),
	]

