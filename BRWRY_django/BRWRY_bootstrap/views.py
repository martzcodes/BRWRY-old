from django.shortcuts import render_to_response
from django.template.context import RequestContext
from BRWRY_bootstrap.forms import BRWRYForm, BRWRYTest, HardwareForm, InstructionForm
from BRWRY_bootstrap.models import Hardware, Instruction
from BRWRY_django.BRWRY_bootstrap.forms import BRWRYModelForm, BRWRYInlineForm, WidgetsForm
from BRWRY_django.BRWRY_bootstrap.updateInstruction import updateInstruction, updateName

def BRWRY_configure(request):
    hardware = Hardware.objects.get(pk=1)
    if request.method == 'POST':
        form = HardwareForm()
        form = HardwareForm(request.POST,instance=hardware)
#        form = HardwareForm(request.POST)
        if form.is_valid():
	        form.save()
    else:
        form = HardwareForm()
        form = HardwareForm(instance=hardware)
    return render_to_response('configure.html', RequestContext(request, {
        'form': form,
        'hardware': hardware,
    }))

def BRWRY_index(request):
    hardware = Hardware.objects.get(pk=1)
    instructions = Instruction.objects.get(pk=1)
    brwName = request.GET.get('name')
    if (brwName != None):
        updateName(brwName)
    if request.method == 'POST':
        form = InstructionForm()
        form = InstructionForm(request.POST,instance=instructions)
        if form.is_valid():
            form.save()
            post = request.POST.copy()
            updateInstruction(post)
    else:
        form = InstructionForm()
        form = InstructionForm(instance=instructions)
    return render_to_response('index.html', RequestContext(request, {
        'form': form,
        'hardware': hardware,
        'instructions':instructions,
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