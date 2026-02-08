from app_settings import AppSettings
from langchain.agents import create_agent

# Loading dev settings
app_settings = AppSettings(env_file='config/dev.env')

def get_weather(city: str) -> str:
    return f"It's always sunny in {city}"


agent = create_agent(
    model = "claude-opus-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

agent.invoke(
    {"messages": [{"role": "user", "content":"what is the weather in sf"}]}
)



