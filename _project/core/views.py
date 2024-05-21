from django.shortcuts import render,redirect
from .models import Activity, TimeLog
from datetime import datetime

# Create your views here.
def index(req):
    activities=Activity.objects.all()
    return render(req,'core/index.html',{"activities":activities,"title":"Activity Tracker"})

def newActivity(req):
    return render(req,'core/newActivity.html',{"title":"Create New Activity"})

def createNewActivity(req):
    activity = Activity(
        name=req.POST.get('name','')
    )
    activity.save()
    return redirect('/')

def showActivity(req,id):
    activity=Activity.objects.get(pk=id)
    timeLogs = TimeLog.objects.filter(activity_id=id)
    #all, getquery set
    return render(req,'core/activity.html',{"activity":activity, "timeLogs":timeLogs})

def createTimeLog(req, id):
    activity=Activity.objects.get(pk=id)
    return render(req,'core/newTimeLog.html',{"activity":activity})

def newTimeLog(req,id):
    timeLog = TimeLog(
        start_time= req.POST.get('startTime',''),
        end_time=req.POST.get('endTime',''),

        activity=Activity.objects.get(pk=id)
        #idk if it should be activiy or activityid
    )
    timeLog.save()
    return redirect(f'/activity/{id}/')