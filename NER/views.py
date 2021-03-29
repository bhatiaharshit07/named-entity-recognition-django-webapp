from django.shortcuts import render
import spacy
# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    ans = request.GET['input_text']
    ans2 = request.GET['input_text2']

    nlp = spacy.load("en_core_web_sm")
    text1 = nlp(ans2)
    nerList = []
    for word in text1.ents:
        print(word.text,word.label_)
        nerList.append([word.text])
    HELL = [[10,11],12]
    return render(request, "result.html", {'ans':ans, 'ans2':text1.ents})
