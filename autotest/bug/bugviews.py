from django.shortcuts import render
from .models import Bug


# Create your views here.

# bug 管理
def bug_manage(request):
    bug_list = Bug.objects.all()
    username = request.session.get('user', '')
    return render(request, 'bug_manage.html', {'user': username, 'bugs': bug_list})
