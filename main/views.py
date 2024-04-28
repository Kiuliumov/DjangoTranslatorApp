from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from translate import Translator

# Create your views here.

from django.shortcuts import render
from translate import Translator


from django.shortcuts import render
from translate import Translator

def home(request):
    if request.method == "POST":

        text = request.POST.get("translate", "")
        language = request.POST.get("language", "")
        if text:
            translator = Translator(to_lang=language)
            translation = translator.translate(text)
            return render(request, "main/translation_result.html", {"translation": translation})

    return render(request, "main/index.html")