# I have created this file  -- Saim
from django.shortcuts import render
from django.http import HttpResponse

# Code for video: 6
def index(request):
	params={'name':'Saim' , 'place':'Khaplu'}
	return render(request,"index.html",params )

def analyze(request):

	dJtext=request.GET.get('text','default')
	removepunc = request.GET.get('removepunc','off')
	fullcaps = request.GET.get('fullcaps','off')
	newlineremover = request.GET.get('newlineremover','off')
	charcount=request.GET.get('charcount','off')
	extraspaceremo=request.GET.get('extraspaceremo','off')


	print(removepunc)
	print(dJtext )
	if removepunc =="on":
		punctuations='''!()-{}[]:;'"\,<>./?@#$%^&*_~'''
		analyzed=""
		for char in dJtext:
			if char not in punctuations:
				analyzed = analyzed + char

		params={'purpose':'removed Punctuations','analyzed_text':analyzed}
		dJtext=analyzed
		# return render(request,'analyze.html',params)
	
	if fullcaps=="on":
		analyzed=""
		for char in dJtext:
			analyzed=analyzed + char.upper()
		params={'purpose':'change into Uppercase latter','analyzed_text':analyzed}
		dJtext=analyzed
		# return render(request,'analyze.html',params)
	

	if (newlineremover=="on"):
		analyzed=""
		for char in dJtext:
			if char !="\n" and char!="\r":
				analyzed=analyzed + char
		params={'purpose':'removed new line','analyzed_text':analyzed}
		dJtext=analyzed
		# return render(request,'analyze.html',params)
	
	if (charcount=='on'):
		analyzed=len(dJtext)
		params={'purpose':'Count the no of character','analyzed_text':analyzed}
		dJtext=analyzed
		# return render(request,'analyze.html',params)

	if (extraspaceremo=="on"):
		analyzed=""
		for index, char in enumerate(dJtext):
			if not(dJtext[index]==" "and dJtext[index+1]==" "):
				analyzed=analyzed+char
		params={'purpose':'removed new line','analyzed_text':analyzed}
		dJtext=analyzed
		# return render(request,'analyze.html',params)

	if (charcount!="on" and extraspaceremo!="on" and newlineremover !="on" and fullcaps!="on" and removepunc!="on"):
	 	return HttpResponse("pleace select any operation")


	return render (request,'analyze.html',params)

# def home(request):
#     return HttpResponse(''' <h1>About iftikhar Saim</h1>''')
# def home (request):
# 	return HttpResponse("Home")



# def capfirst (request):
# 	return HttpResponse('''<h1>capfirst</h1> <a href="/newlineremove/">Next</a> ''')
	

# def newlineremove (request):
# 	return HttpResponse('''<h1>newlineremove</h1> <a href="/spaceremove/">Next</a> ''')
	

# def spaceremove (request):
# 	return HttpResponse('''<h1>spaceremove</h1> <a href="/charcount/">Next</a> ''')
	

# def charcount (request):
# 	return HttpResponse('''<h1>charcount</h1> <a href="/about/">Back to about</a> ''')
	
