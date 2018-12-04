from django.http import Http404, HttpResponse

import datetime
def datetimeoffset(req):
    return HttpResponse('lili')
def hourahead(req, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html='hours %s offset is %s'% (offset, dt)
    return HttpResponse(html)
from django.shortcuts import render
def search_form(request):
    return render(request, 'search_form.html')

from books.models import Book
# ...
def search(request):
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                      {'books': books, 'query': q})
    else:
        return render(request, 'search_form.html',
                      {'error': errors})