from django.shortcuts import render
from .models import *
import datetime
# Create your views here.
def index(request):
	now = datetime.datetime.now()
	earlier = now - datetime.datetime(now.year, now.month, now.day, now.hour, 0,0)
	datas = DSE.objects.all().order_by('-created_at')
	print(datas)
	return render(request, "index.html",{'datas':datas})
