from django import forms


class SiteToScrapeForm(forms.Form):
    url = forms.URLField()