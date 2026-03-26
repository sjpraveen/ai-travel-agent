from langchain_core.messages import HumanMessage, AIMessage
from src.agents.travel_agent import agent
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException


logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self):
        self.messages = []
        logger.info("TravelPlanner initialized successfully.")

    def create_itinerary(self, 
                         city: str,
                         days: int,
                         interests: list[str],
                         style: str,
                         pace: str,
                         month: str | None = None):
        try:
            user_prompt = f"""
            Plan a {days}-day trip to {city} for someone interested in {', '.join(interests)}
            with a {style} travel style and a {pace} pace. The trip is planned for {month if month else 'an unspecified month'}
            . Provide a detailed day-wise itinerary including activities, dining, and accommodation recommendations.
            """
            self.messages.append(HumanMessage(content=user_prompt.strip()))
            response = agent.invoke({"messages": self.messages})
            final_answer = response["messages"][-1].content
            self.messages.append(AIMessage(content=final_answer))
            return final_answer
        except Exception as e:
            logger.error(f"Error creating itinerary: {e}")
            raise CustomException(f"An error occurred while creating the itinerary: {e}")
