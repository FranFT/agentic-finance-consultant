from app_settings import AppSettings
from document_loader import DocumentLoader

from langchain_google_genai import ChatGoogleGenerativeAI

# Loading dev settings
app_settings = AppSettings(env_file='config/dev.env')

# Document loader
loader = DocumentLoader('input/invoice-0-4.pdf')

print(loader.get_document_text())

# Define Gemini Model
model = ChatGoogleGenerativeAI(
    model=app_settings.google_gemini_model_name,
)

message = [
    (
        "system",
        "You are an expert financial audit consultant. Your goal is to analyze invoice data and detect potential irregularities.",
    ),
    (
        "human",
        f"I received an invoice {loader.docs[0]}. Does it seem suspicious to you? Justify your answer."
    ),
]

ai_msg = model.invoke(message)
print(ai_msg)

