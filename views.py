from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    rmpunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    numremove = request.GET.get('numremove', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    expacerem = request.GET.get('expacerem', 'off')
    charcount = request.GET.get('charcount', 'off')
    reverse = request.GET.get('reverse', 'off')

    punctuations = '''!@#$%^&*()_+|/-?>.="\ }{"<:;[]`~'''
    analyzed = ""
    
    if rmpunc == "on":

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        
        params = {'purpose': 'removed punctuations', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # if capitalize is on
    elif fullcaps == "on":
        analyzed = ""

        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'changed to uppercase', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":

                analyzed = analyzed + char
        params = {'purpose': 'changed to uppercase', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif expacerem == "on":
        analyzed = ""

        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
                
        params = {'purpose': 'some shit', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif numremove == "on":
        analyzed = ""
        nums = '1234567890'
        for char in djtext:
            if char not in nums:
                analyzed = analyzed + char
        params = {'purpose': 'numbers removed', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif charcount == "on":
        index = 0
        for char in djtext:
            index += 1
            analyzed = index

        params = {'purpose': 'counted characters', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif reverse == "on":
        analyzed = ""
        revstr = djtext[::-1]
        analyzed = revstr

        params = {'purpose': 'String reversed', 
        'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        
        

    else:
        return HttpResponse("Error: 434\nPlease choose a valid option.")

# 100 complete