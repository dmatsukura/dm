from dm_portfolio.models import Portfolio
from django.views import generic
# Create your portflio view logic here.

class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "dm_portfolio/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)
	
class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "dm_portfolio/portfolio-detail.html"



	

