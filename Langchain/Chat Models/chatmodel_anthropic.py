from langchain_antropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude-3.5-sonnet-20241022')
result=model.invoke('what is the temperature in thane right now?') #very descriptive output
print(result.content)