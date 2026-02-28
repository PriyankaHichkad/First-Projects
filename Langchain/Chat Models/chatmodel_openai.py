from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=2)
result=model.invoke("what is the temperature in mumbai right now")
print(result) #Provides answer+metadata
print(result.content)