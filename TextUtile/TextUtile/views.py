#I have created this file - Yadul
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on" and(len(djtext)>0):
        punctuations = '''!()-[]{};:'"\,<>.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error!")