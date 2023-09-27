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
from django.http import HttpResponse


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@api_view(['POST'])

def generate_questions(request):
    text_data = request.data.get('text', '')
    # Add your logic to interact with OpenAI API and generate questions
    questions = [f"Placeholder question based on the text: {text_data}"]
    return Response({'questions': questions})

@api_view(['POST'])

def generate_questions(request):
    text_data = request.data.get('text', '')
    # Add your logic to interact with OpenAI API and generate questions
    questions = [f"Placeholder question based on the text: {text_data}"]
    return Response({'questions': questions})

@api_view(['POST'])

def upload_file(request):
    try:
        #print(text)
        text ="hi"
        file = request.FILES['file']
        # Save the uploaded file temporarily
    
        temp_filename = file.name
        with open(temp_filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        try:
            # Extract text from the saved PDF file
            text = extract_text(temp_filename)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        finally:
            # Delete the temporary file
            os.remove(temp_filename)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=" 5 questions each with 4 choices and right answer for following content: " + text,
            temperature=0.7,
            max_tokens=1000
        )
        print(response.choices[0])

        response_text = response.choices[0].text.strip()

        # Here we assume that the response_text has a very specific and consistent format
        # You will need to modify the parsing logic to suit the exact format of your response_text
        print(response_text)
        questions = response_text.split("\n")
        #questions_data = []
        print(questions)
        return Response({"response": questions}, status=status.HTTP_200_OK)

        #return Response({"response": response.choices[0].text.strip()}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def test_openai(request):
    return Response({'text'})
