# coding: utf-8
from __future__ import unicode_literals

from django import template
from django.core.urlresolvers import reverse
from django.utils.http import urlencode

from ..models import Lead

register = template.Library()


@register.inclusion_tag('hypnobox/_link.html', takes_context=True)
def new_lead(context, product_id, media=''):
    link = reverse('{}:new_lead'.format(Lead._meta.app_label))
    params = urlencode(dict(product_id=product_id, media=media))
    return {
        'url': "{}?{}".format(link, params),
    }
