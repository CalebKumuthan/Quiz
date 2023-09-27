from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import openai
from dotenv import load_dotenv
import os
from pdfminer.high_level import extract_text
from django.core.files.storage import default_storage
from rest_framework import status

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@api_view(['POST'])

def is_api_key_valid():
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt="This is a test.",
            max_tokens=5
        )
    except:
        return False
    else:
        return True

def generate_questions(request):
    text_data = request.data.get('text', '')
    # Add your logic to interact with OpenAI API and generate questions
    questions = [f"Placeholder question based on the text: {text_data}"]
    return Response({'questions': questions})

@api_view(['POST'])
def upload_file(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    text = extract_text(file_path)

    # Check the validity of the API key
    api_key_valid = is_api_key_valid()
    print("API key is valid:", api_key_valid)

    #os.remove(file_path)  # Delete the file after extracting text
    try:
        #print(text)
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            temperature=0.7,
            max_tokens=150
        )
        print(response)
        return Response({"response": response.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


   # return Response({'text': text})
