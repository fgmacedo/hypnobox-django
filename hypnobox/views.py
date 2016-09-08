# -*- coding: utf-8 -*-
from django.views.generic import CreateView


from .models import Lead
from .forms import LeadForm
from . import settings as app_settings


class LeadCreateView(CreateView):
    form_class = LeadForm
    model = Lead

    def get_form_kwargs(self):
        kwargs = super(LeadCreateView, self).get_form_kwargs()
        initial = {
            'product_id': self.request.GET.get('product_id'),
            'media': self.request.GET.get('media'),
        }
        kwargs['initial'] = initial
        return kwargs

    def get_success_url(self):
        params = self.object.as_params()
        url = app_settings.SUCCESS_URL.format(
            client_id=app_settings.CLIENT_ID,
            domain=app_settings.DOMAIN,
            params=params
        )
        return url
