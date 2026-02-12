from app_settings import AppSettings
from document_loader import DocumentLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from invoice_model import Invoice

# Loading dev settings
app_settings = AppSettings(env_file='config/dev.env')

# Document loader
loader = DocumentLoader('input/invoice-0-4.pdf')

# Define Gemini Model
llm = ChatGoogleGenerativeAI(model=app_settings.google_gemini_model_name)

# Create agent
agent = create_agent(
    model=llm,
    response_format=Invoice,
    system_prompt="You are an expert financial audit consultant. Your goal is to extract and analyze invoice data and detect potential irregularities."
)

# Running agent
result = agent.invoke({
    "messages": [{"role": "user", "content": f"I received the following invoice {loader.get_document_text()}. Does it seem suspicious to you? Justify your answer."}]
})

print(result["structured_response"])
