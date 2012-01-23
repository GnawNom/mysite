from django.shortcuts import render_to_response, HttpResponse
import datetime

def hello(request):
	return HttpResponse("Hello World!")

def current_datetime(request):
	now=datetime.datetime.now()
	
	return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
	try:
		offset=int(offset)
	except:
		raise Http404()
	ctx={'next_time': datetime.datetime.now()+ datetime.timedelta(hours=offset),
		'hours_offset':offset}
	next_time=datetime.datetime.now()+ datetime.timedelta(hours=offset)
	hours_offset=offset
	#html="<html><body>In %s hours it will be %s </body></html>" %(offset,next_time)
	#return HttpResponse(html)
	return render_to_response('hours_ahead.html', ctx)

def header(request):

	tags = request.META.items()
	pstring=""
	html =[]
	keys=[]
	values=[]
	for k,v in tags:
		#html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
		keys.append(k)
		values.append(v)


	#return HttpResponse('<table>%s</table>' % '\n'.join(html))
	
	secure = request.is_secure()
	return render_to_response('header.html', {'keys':keys,'values':values , 'dict':tags, 'secure':secure})


