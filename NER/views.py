from django.http.response import HttpResponse
from django.shortcuts import render
import spacy
from spacy import displacy
# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):

    input_sentence = request.GET['input_text']

    nlp = spacy.load("en_core_web_sm")
    text = nlp(input_sentence)
    nerList = []
    for word in text.ents:
        print(word.text,word.label_)
        nerList.append([word.text,word.label_])
    html = displacy.render([text], style="ent", page=True)
    return HttpResponse(html[308:-7])
    #return render(request, "result.html", {'ans':text, 'ans2':nerList, 'content':html})
    #return HttpResponse("<h1>hello</h1>")