from django.shortcuts import render_to_response
from django.template.context import RequestContext
from BRWRY_bootstrap.forms import BRWRYForm, BRWRYTest
from BRWRY_django.BRWRY_bootstrap.forms import BRWRYModelForm, BRWRYInlineForm, WidgetsForm

def BRWRY_configure(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        valves = request.POST.getlist(u'valves')
        if not valves:
            valves = ''
        elements = request.POST.getlist(u'heating')
        if not elements:
            elements = ''
        sensors = request.POST.getlist(u'sensors')
        if not sensors:
            sensors = ''
        pumps = request.POST.getlist(u'pumps')
        if not pumps:
            pumps = ''
        form = BRWRYTest(request.POST)
    else:
        sensors = ''
        elements = ''
        valves = ''
        pumps = ''
        form = BRWRYTest()
    modelform = BRWRYModelForm()
    return render_to_response('configure.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'valves': valves,
        'elements': elements,
        'sensors': sensors,
        'pumps': pumps,
    }))

def BRWRY_form_with_template(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = BRWRYForm(request.POST)
        form.is_valid()
    else:
        form = BRWRYForm()
    modelform = BRWRYModelForm()
    return render_to_response('form_using_template.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))

def BRWRY_form(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = BRWRYForm(request.POST)
        form.is_valid()
    else:
        form = BRWRYForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'test':'This is a test',
        }))

def BRWRY_form_inline(request):
    layout = request.GET.get('layout', '')
    if layout != 'search':
        layout = 'inline'
    form = BRWRYInlineForm()
    return render_to_response('form_inline.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))

def BRWRY_tabs(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'tabs'
    tabs = [
        {
            'link': "#",
            'title': 'Tab 1',
        },
        {
            'link': "#",
            'title': 'Tab 2',
        }
    ]

    return render_to_response('tabs.html', RequestContext(request, {
        'tabs': tabs,
        'layout': layout,
    }))

def BRWRY_widgets(request):
    layout = request.GET.get('layout', 'vertical')
    form = WidgetsForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))