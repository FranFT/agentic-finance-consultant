from app_settings import AppSettings
from langchain_google_genai import ChatGoogleGenerativeAI

# Loading dev settings
app_settings = AppSettings(env_file='config/dev.env')

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
        "I received an invoice for €5,500 for 'coffee consulting services' on a Sunday. Does it seem suspicious to you? Justify your answer."
    ),
]

ai_msg = model.invoke(message)
print(ai_msg)