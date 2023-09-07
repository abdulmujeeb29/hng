from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta
import pytz 
# Create your views here.
def get_info(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')

    current_day = datetime.now().strftime('%A')
    utc_time = datetime.now(pytz.UTC)
    validated_time = 'True'

    if validated_time:
        utc_time += timedelta(minutes=2)

    github_file_url =''
    github_repo_url =''

    response = {
        "slack_name" : slack_name,
        "current_day" :current_day,
        "utc_time": utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track" : track,
        "github_file_url": "",
        "github_repo_url" : "",
        "status_code" : 200
        

    }

    return JsonResponse(response)