import os

from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from django.views.generic import ListView, View

from .parser import parse_page


def manualpage(request, requestpath):
    """
    Load the markdown file `requestpath`.md or `requestpath/index.md` if folder.
    Apply `process_webcopy_html` transformations to prepends `/webcopy` to links.
    """
    if len(requestpath) == 0:   # handle / correctly
        requestpath = 'index'
    if requestpath.endswith('/'):
        requestpath = requestpath.rstrip('/')
    mdfilename = requestpath.rstrip('/') + '.md'
    mdfullpath = os.path.join(settings.MARKDOWN_PAGES, mdfilename)
    # if not a full path
    if not os.path.exists(mdfullpath):
        # try folder
        mdfilename = requestpath + '/index.md'
        mdfullpath = os.path.join(settings.MARKDOWN_PAGES, mdfilename)
        if not os.path.exists(mdfullpath):
            # else bail
            return HttpResponseNotFound('<h1>404: Page not found</h1>')

    content_html = None
    with open(mdfullpath) as mdfile:
        contents = mdfile.read()
        links, html = parse_page(contents)
    template = get_template('website/manualpage.html')
    context =  {
        'requestpath': requestpath,
        'mdfilename': mdfilename,
        'content_html': html,
        'metadata': links,
    }
    return HttpResponse(template.render(context, request))

