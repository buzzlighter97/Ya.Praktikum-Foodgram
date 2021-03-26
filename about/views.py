from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'flatpages/about/author.html'


class SpecView(TemplateView):
    template_name = 'flatpages/about/spec.html'
