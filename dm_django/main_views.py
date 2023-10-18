from django.shortcuts import render
from django.contrib import messages
from dm_portfolio.models import Blog, Portfolio, Testimonial, Certificate
from django.views import generic
from dm_django.forms import ContactForm


class MainView(generic.TemplateView):
    template_name = "dm_django/main_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context

class ContactView(generic.FormView):
    template_name = 'dm_django/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. Email sent successfully')
        return super().form_valid(form)
    
class BlogView(generic.ListView):
	model = Blog
	template_name = "dm_django/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)
     

class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "dm_django/blog-detail.html"