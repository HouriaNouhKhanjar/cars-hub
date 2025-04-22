from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.shortcuts import render
from django.http import Http404


def error_400(request, exception):
    return render(request, '400.html', status=400)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)


def forbiden(request):
    raise PermissionDenied


def bad_request_view(request):
    raise SuspiciousOperation("Simulated 400 error")


def crash_view(request):
    raise Exception("Something went wrong")


def not_found(request):
    raise Http404("Page not found")