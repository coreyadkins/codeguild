"""multimadlib Views."""

from django.shortcuts import render
from django.template.base import VariableNode
from django.http import HttpResponse
from django.template import Context, Template
from . import models


def _var_names_in_template(template):
    """Returns a list of all variables names used in a template."""
    return [
        node.filter_expression.var.var
        for node
        in template.compile_nodelist().get_nodes_by_type(VariableNode)
    ]

def render_index(request):
    """Renders the index which contains links to all forms."""
    arguments = {
        'madlibs': models.access_all_madlibs
    }
    return render(request, 'multimadlib/index.html', arguments)


def render_new_madlib(request):
    """Renders the form to create a new madlib."""
    return render(request, 'multimadlib/new_madlib.html')


def render_new_madlib_ack(request):
    """Uses the POST data to create madlib, then renders a page acknowledging successful submission, or returns
    a message if there are missing fields.
    """
    name = request.POST['name']
    template = Template(request.POST['template'])
    try:
        models.create_new_madlib(name, template)
    except KeyError:
        return HttpResponse('Missing fields', status=400)
    return render(request, 'multimadlib/new_madlib_ack.html')


def render_madlib_form(request, madlib_name):
    """Renders the form to input completions to the variables in template."""
    madlib = models.access_madlib_by_name(madlib_name)
    var_names = _var_names_in_template(madlib['template'])
    arguments = {
        'madlib_name': madlib['name'],
        'variables': var_names
    }
    return render(request, 'multimadlib/madlib_form.html', arguments)


def render_madlib_display(request, madlib_name):
    """Renders completed madlib."""
    madlib = models.access_madlib_by_name(madlib_name)
    template = madlib['template']
    var_names = _var_names_in_template(template)
    madlib_variables_to_completions = {}
    for name in var_names:
        madlib_variables_to_completions.update({name: request.GET[name]})
    context = Context(madlib_variables_to_completions)
    return template.render(context)
