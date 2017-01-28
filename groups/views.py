from django.shortcuts import render
from django.views.generic import View

class GroupListView(View):
    def get(self, request):
        return render(request, 'groups/groups.html')
