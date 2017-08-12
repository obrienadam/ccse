from django.views.generic import ListView, DetailView

import models

class GroupListView(ListView):
    template_name = 'research/groups.html'
    queryset = models.Group.objects.all()
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    template_name = 'research/group.html'
    model = models.Group
    context_object_name = 'group'
    slug_field = 'slug'

class FieldListView(ListView):
    template_name = 'research/fields.html'
    queryset = models.Field.objects.all()
    context_object_name = 'fields'

class FieldDetailView(DetailView):
    template_name = 'research/field.html'
    model = models.Field
    context_object_name = 'field'
