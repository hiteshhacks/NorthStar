 
from app.schemas.explain import ExplainRequest
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

Client  = Groq(api_key=os.getenv("GROQ_API"))
MODEL = "openai/gpt-oss-120b"

 

def prompt_builder(dp,di):
    return f""" 
You are a AI Ethics Expert
Analyze the following fairness metrics:

Demographic Parity:
{dp}

Disparate Impact:
{di}

        if di< 0.8:
            risk = "HIGH"
        elif di< 0.9:
            risk = "MEDIUM"
        else:
            risk = "LOW"

Your task:
1. Explain whether the model is biased or fair
2. Identify which group is disadvantaged
3. Classify risk level (LOW / MEDIUM / HIGH)
4. Give clear, practical suggestions to reduce bias

Keep explanation simple and structured.
    

    """


 





    

     