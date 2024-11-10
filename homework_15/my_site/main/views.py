from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from .dataset import DESCRIPTION, COMPANY_NAME, SERVICES_LIST, CONTACTS


def home(request):
    count_services = len(SERVICES_LIST)
    context = {
        "title": "Головна",
        "count_services": count_services,
        "company_name": COMPANY_NAME,
    }
    return render(request, "main/home.html", context=context)


def about(request):
    last_updated = datetime.now()
    html_content = "<strong>Це важлива інформація</strong>"

    context = {
        "title": "Про ВРЦОЯО",
        "last_updated": last_updated,
        "description_company": DESCRIPTION,
        "company_name": COMPANY_NAME,
        "html_content": html_content,
    }
    return render(request, "main/about.html", context=context)


class ContactView(TemplateView):
    template_name = "main/contact.html"
    extra_context = {
        "title": "Контакти",
        "contacts": CONTACTS,
    }


class ServiceView(TemplateView):
    template_name = "main/services.html"
    extra_context = {
        "title": "Послуги",
        "services_list": SERVICES_LIST,
    }
