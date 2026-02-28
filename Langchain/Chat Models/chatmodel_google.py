from langchain_google_genai import ChatGoogleGenarativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenarativeAI(model='genimi-1.5-pro')
result=model.invooke('who is the most famous indian actress')
print(result.content)