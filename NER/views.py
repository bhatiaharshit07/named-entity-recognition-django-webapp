
from django.shortcuts import render
import spacy
from spacy import displacy
# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):

    input_sentence = request.POST.get('input_text')

    nlp = spacy.load("en_core_web_md")
    text = nlp(input_sentence)
    
    ent_list = request.POST.getlist('check')
    if len(ent_list) == 0:
        option = {"ents":None}
    else:    
        option = {"ents":ent_list}

    html = displacy.render([text], style="ent", options=option)
    return render(request, "result.html", {'content':html})