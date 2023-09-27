from django.test import TestCase
import os

# Create your tests here.
import openai

# Set your OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = os.getenv()

# Define the past financial data and context for the AI model
past_data = """
Month,Revenue,Expenses,Profit
January,10000,6000,4000
February,12000,7000,5000
March,11000,6500,4500
April,13000,7500,5500
May,14000,8000,6000
"""

# Create a prompt for the AI model
prompt = f"Based on the following past financial data, predict the revenue, expenses, and profit for the upcoming months and generate insights:\n{past_data}\n\n"

# Generate financial forecasts and reports using OpenAI API
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=150,  # Adjust as needed
    temperature=0.7,  # Adjust for creativity vs. accuracy
    n = 1, # Generate a single response
)

# Extract the AI-generated financial forecasts and reports
generated_text = response.choices[0].text

# Print the generated financial forecasts and reports
print(generated_text)