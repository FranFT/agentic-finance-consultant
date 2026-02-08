from app_settings import AppSettings
from langchain_google_genai import ChatGoogleGenerativeAI

# Loading dev settings
app_settings = AppSettings(env_file='config/dev.env')

# Define Gemini Model
model = ChatGoogleGenerativeAI(
    model='gemini-flash-lite-latest',
)

message = [
    (
        "system",
        "You are a helpful assitant that translates English to French. Translate the user sentence.",
    ),
    (
        "human",
        "I love programming."
    ),
]

ai_msg = model.invoke(message)
print(ai_msg)