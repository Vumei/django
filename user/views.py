from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic
from .forms import TopicForm

def index(request):
	return render(request,'user/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request,'user/topics.html',context)

def topic(request,topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'user/topic.html',context)

def new_topic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('user:topics'))
	context = {'form':form}
	return render(request,'user/new_topic.html',context)