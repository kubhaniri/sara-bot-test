from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import wikipedia
import re

class ActionWIki(Action):

    def name(self) -> Text:
        return "action_wiki"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message.get('text')
        message = re.sub('wiki ', '', message)

        dispatcher.utter_message(text=wikipedia.summary(message))

        return []
