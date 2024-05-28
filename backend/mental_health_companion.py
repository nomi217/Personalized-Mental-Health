import openai
import os
from dotenv import find_dotenv, load_dotenv

_ : bool = load_dotenv(find_dotenv()) #read local .env file
#find_dotenv()

class MentalHealthCompanion:
    def __init__(self):
        openai.api_key= os.getenv("OPENAI_API_KEY") #call open ai

    
    def assess_mental_health(self, input_text):
        response = openai.chat.completions.create(
            model="gpt-4o",
            engine="text-davinci-003",
            prompt=f"Assess the following input for mental health concerns: {input_text}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    
    def chat_emotional_support(self, input_text):
        sentiment_response = openai.Completion.create(
            model="gpt-4o",
            engine="text-davinci-003",
            prompt=f"Analyze the sentiment of the following text: {input_text}",
            max_tokens=50
        )
        sentiment = sentiment_response.choices[0].text.strip()

        if "positive" in sentiment:
            return "I'm glad to hear you're feeling positive! How can I help you today?"
        elif "negative" in sentiment:
            return "I'm sorry to hear you're feeling down. Here are some coping strategies that might help..."
        else:
            return "Tell me more about how you're feeling."