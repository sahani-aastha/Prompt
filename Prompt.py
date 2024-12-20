import google.generativeai as genai
from IPython.display import HTML, Markdown, display

#--------------------------------------API---------------------------------------------

#from kaggle_secrets import UserSecretsClient
#secret_label = "your-secret-label"
#secret_value = UserSecretsClient().get_secret(secret_label)

API_KEY = "AIzaSyCjYUc1M2DRIWxcomFYHD-pO1yJK4Rhn_Y"
genai.configure(api_key=API_KEY)


flash = genai.GenerativeModel('gemini-1.5-flash')
"""response = flash.generate_content("Explain AI to me like I'm an adult.")
print(response.text)"""


chat = flash.start_chat(history=[])
response = chat.send_message('Hello! My name is Bijan.')
print(response.text)

#------------------------------------------Parameters------------------------------------

model = genai.GenerativeModel(
    'gemini-1.5-flash-001',
    generation_config=genai.GenerationConfig(
        temperature=0.1,
        top_p=1,
        max_output_tokens=5,
    ))

zero_shot_prompt = """Classify movie reviews as POSITIVE, NEUTRAL or NEGATIVE.
Review: "Her" is a disturbing study revealing the direction
humanity is headed if AI is allowed to keep evolving,
unchecked. I wish there were more movies like this masterpiece.
Sentiment: """

response = model.generate_content(zero_shot_prompt, request_options=retry_policy)
print(response.text)

#-----------------------------------------ENUM----------------------------------------

import enum

class Sentiment(enum.Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


model = genai.GenerativeModel(
    'gemini-1.5-flash-001',
    generation_config=genai.GenerationConfig(
        response_mime_type="text/x.enum",
        response_schema=Sentiment
    ))

response = model.generate_content(zero_shot_prompt, request_options=retry_policy)
print(response.text)

#-----------------------------------------CODE GENERATION-------------------------------------

model = genai.GenerativeModel(
    'gemini-1.5-flash-latest',
    tools='code_execution',)

code_exec_prompt = """
Calculate the sum of the first 14 prime numbers. Only consider the odd primes, and make sure you count them all.
"""

response = model.generate_content(code_exec_prompt, request_options=retry_policy)
Markdown(response.text)