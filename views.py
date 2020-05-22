from .models import Meeting, MeetingMinutes, Resource, Event

from django.shortcuts import get_object_or_404

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pythonclubapp/index.html')


def getresources(request):
    resource_list = Resource.objects.all()
    return render (request, 'pythonclubapp/resources.html', {'resource_list' : resource_list})


def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render (request, 'pythonclubapp/meetings.html',{'meetings_list': meetings_list,})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet': meet,
    }
    return render(request, 'pythonclubapp/meetingdetails.html', context=context)
