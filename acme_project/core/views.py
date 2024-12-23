from django.shortcuts import render


# Create your views here.
def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)

def csrf_failure(request, *args, **kwargs):
    return render(request, 'core/403csrf.html', status=403)
