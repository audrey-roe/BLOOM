import io 
from xhtml2pdf import pisa
from django.http import HttpResponse
from html import escape

from django.template.loader import render_to_string

def render_to_pdf(template_src, context_dict):
    html = render_to_string(template_src, context_dict)
    result = io.BytesIO()



    pdf = pisa.pisaDocument(io.BytesIO (html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))