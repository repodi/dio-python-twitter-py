from typing import Any, Dict, List

import tweepy
from src.ConfigurationLoader import ConfigurationLoader as configuration

from src.connection import trends_collection
from src.constants import BRAZIL_WOE_ID


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = api.trends_place(woe_id)

    return trends[0]["trends"]


def get_trends() -> List[Dict[str, Any]]:
    """Get treending topics persisted in MongoDB.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    """Get trends topics and save on MongoDB."""
    CONSUMER_KEY = configuration.get_value_environment(key="CONSUMER_KEY")
    CONSUMER_SECRET = configuration.get_value_environment(key="CONSUMER_SECRET")
    ACCESS_TOKEN = configuration.get_value_environment(key="ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = configuration.get_value_environment(key="ACCESS_TOKEN_SECRET")
    
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)
