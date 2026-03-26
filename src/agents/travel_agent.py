from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from src.tools.tavily_tool import tavily_search_tool
from src.tools.serper_tool import google_serper_search_tool
from src.config.config import GROQ_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Initialize the chat model with the specified parameters
model = init_chat_model(model="llama-3.1-8b-instant",
                        model_provider="groq",
                        temperature=0.3)

SYSTEM_PROMPT = """
You are an expert AI travel planner.

Rules:
1. Always use the provided tools to gather information before answering any questions.
2.Create a detailed day-wise itinerary for a trip based on the user's preferences and constraints.
3. Include recommendations for activities, dining, and accommodations in the itinerary.
4. Ensure that the itinerary is realistic and feasible within the given time frame and budget.

User Inputs:
- Destination: The location where the user wants to travel.
- days: The number of days the user plans to spend at the destination.
- Interests: The user's interests (e.g., culture, adventure, relaxation).
- style: The user's preferred travel style (e.g., luxury, budget, family-friendly).
- pace: The user's preferred pace of travel (e.g., relaxed, moderate, fast-paced).
- month: The month of travel (optional, but can help in providing season-specific recommendations).
"""


agent = create_agent(
    model=model,
    tools=[tavily_search_tool, google_serper_search_tool],
    system_prompt=SYSTEM_PROMPT.strip()
)

logger.info("Travel agent initialized successfully.")

