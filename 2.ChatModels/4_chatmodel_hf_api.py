from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Load .env
load_dotenv()

# Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3.8-27B",
    task="text-generation",
    max_new_tokens=100,
    temperature=0.7,
)

# Convert LLM into Chat Model
model = ChatHuggingFace(llm=llm)

# Invoke model
result = model.invoke("Who is prime minister of india ")

print(result.content)