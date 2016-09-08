# coding: utf-8

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


SPEC_VERSION = getattr(settings, 'HYPNOBOX_SPEC_VERSION', 1.0)
DOMAIN = getattr(settings, 'HYPNOBOX_DOMAIN', 'hypnobox.com.br')
CLIENT_ID = getattr(settings, 'HYPNOBOX_CLIENT_ID', 'demo')


if SPEC_VERSION == 1.2:
    SUCCESS_URL = 'http://{client_id}.{domain}/?controle=Atendimento&acao=entrar&{params}'
elif SPEC_VERSION == 1.0:
    SUCCESS_URL = 'http://{client_id}.{domain}/atendimento/entrar.php?acao=ENTRAR&{params}'
else:
    raise ImproperlyConfigured(
        'Hypnobox spec version not supported: {}.'.format(SPEC_VERSION))
