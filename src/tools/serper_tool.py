from langchain_community.utilities import GoogleSerperAPIWrapper
from src.config.config import SERPER_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def google_serper_search_tool(query: str) -> str:
    
    """
    Search the web using Google Serper for general travel information.
    """
    try:
        serper = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)
        results = serper.run(query)
        logger.info("Google search completed successfully.")
        return results
    except Exception as e:
        logger.error(f"Error during Serper Google search: {e}")
        return "An error occurred while performing the Google Serpersearch."
    
logger.info("Google Serper Search Tool initialized successfully.")    