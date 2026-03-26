from langchain_tavily import TavilySearch
from src.config.config import TAVILY_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def tavily_search_tool(query: str) -> str:
    
    """
    Search the web using Tavily for travel-related information.
    """
    try:
        tavily = TavilySearch(
            max_results=5,
            topic="general",
            tavily_api_key=TAVILY_API_KEY)
        results = tavily.invoke({"query": query})
        logger.info("Tavily search completed successfully.")
        return results
    except Exception as e:
        logger.error(f"Error during Tavily search: {e}")
        return "An error occurred while performing the Tavily search."
    
logger.info("Tavily Search Tool initialized successfully.")
