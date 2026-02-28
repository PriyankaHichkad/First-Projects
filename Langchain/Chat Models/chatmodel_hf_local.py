from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

os.environ['HF_HOME'] = '' #'address:/huggingface_cache'

llm=HuggingFacePipeline.from_model_id (
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=10
    )
)

model=ChatHuggingFace(llm=llm)
result=model.invooke('who is the most famous indian actress') #very descriptive
print(result.content) #shows user query, answer and source