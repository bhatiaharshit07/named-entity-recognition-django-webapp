from django.http.response import HttpResponse
from django.shortcuts import render
import spacy
from spacy import displacy
# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):

    input_sentence = request.GET['input_text']

    nlp = spacy.load("en_core_web_md")
    text = nlp(input_sentence)
    html = displacy.render([text], style="ent")
    '''
    ex = [{"text": "But Google is starting from behind.",
       "ents": [{"start": 4, "end": 10, "label": "ORG"}],
       "title": None}]
    html = displacy.render(ex, style="ent", manual=True)
    '''
    #return HttpResponse(html[308:-7])
    #return render(request, "result.html", {'ans':text, 'ans2':nerList, 'content':html[344:-25]})
    return render(request, "result.html", {'content':html})