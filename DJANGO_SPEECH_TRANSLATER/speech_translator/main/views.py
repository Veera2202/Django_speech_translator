from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
from googletrans import Translator
import base64
import io

def index(request):
    return render(request, 'index.html')

def recognize_speech(request):
    if request.method == 'POST':
        audio_data = request.POST.get('audio_data', '')

        if not audio_data:
            return JsonResponse({'error': 'No audio data provided'}, status=400)

        audio_data = audio_data.split(',')[1]
        audio_bytes = base64.b64decode(audio_data)
        audio_file = io.BytesIO(audio_bytes)

        try:
            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                return JsonResponse({'text': text})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def translate_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        target_language = request.POST.get('language', '')

        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)

        if not target_language:
            return JsonResponse({'error': 'No target language provided'}, status=400)

        try:
            translator = Translator()
            translated = translator.translate(text, dest=target_language).text
            return JsonResponse({'translated': translated})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def translate_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        target_language = request.POST.get('language', '') 

        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)

        if not target_language:
            return JsonResponse({'error': 'No target language provided'}, status=400)

        try:
            translator = Translator()
            translated = translator.translate(text, dest=target_language).text
            return JsonResponse({'translated': translated})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)