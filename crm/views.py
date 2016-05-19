from django.shortcuts import render
from django.views.generic import base, TemplateView
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class Dashboard(base.View):

    template_name = "crm/dashboard.html"

    def get(self, request):
        return TemplateResponse(request,
                                self.template_name,
                                {})