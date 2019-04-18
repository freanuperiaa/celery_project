from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .forms import SiteToScrapeForm
from .tasks import scrape_site


class HomePageView(FormView):
    form_class = SiteToScrapeForm
    template_name = 'mysite/index.html'

    def form_valid(self, form):
        url_toscrape = form.cleaned_data.get('url')
        #enter task call here
        scrape_site.delay(url_toscrape)
        return redirect('success')


class SuccessQueueTaskView(TemplateView):
    template_name = 'mysite/success.html'
