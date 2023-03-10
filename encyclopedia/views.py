from django.shortcuts import render, redirect
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry):
        if entry not in util.list_entries():
            return render(request, "encyclopedia/error.html", {})
        page = util.get_entry(entry)
        return render(request, "encyclopedia/wiki.html", {"title":entry, "content": Markdown().convert(page)})

def search(request):
    query = request.GET.get('q')
    if query is None or query.isspace()==True:
        return render(request, "encyclopedia/search.html", {"query": query, "matches": ""})
    pages = util.list_entries()
    matches = [
    result
    for result in pages
    if query.upper() in result.upper()]
    return render(request, "encyclopedia/search.html", {"query": query, "matches": matches})
    