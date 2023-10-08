from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import openai
from ChatApp.models import ChatMessage
@csrf_exempt
def my_view(request):
    # Your view logic here
    return HttpResponse("Response from my view")


def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        api_key='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'
        openai.api_key=api_key

        # Use the OpenAI GPT-3 library to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_message,
            max_tokens=1000,
        )
        bot_response = response.choices[0].text

        # Save the user's message and the bot's response to the database
        ChatMessage.objects.create(user=request.user, content=user_message)
        ChatMessage.objects.create(user=None, content=bot_response)

        return render(request, 'ChatApp/chat.html', {'user_message': user_message, 'bot_response': bot_response})
    return render(request, 'ChatApp/chat.html')

from django.http import JsonResponse

def chatgpt_api(request):
    if request.method == 'POST':
        # Your code to communicate with ChatGPT goes here
        chatgpt_response = "This is a sample response from ChatGPT."

        return JsonResponse({'response': chatgpt_response})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

