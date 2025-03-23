from logging import exception

import openai
from django.conf import settings
from openai import OpenAI


class OpenAIClient:
    def __init__(self, model="gpt-4.5-preview-2025-02-27", temperature=0.2, max_tokens=1000):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = OpenAI()
    def get_itinerary(self, destination, travel_type, time, rules):
        text = f"""
        Destination : {destination}
        type of travel: {travel_type}
        time : {time}
        """

        prompt = f"""
        {rules}

        Text: {text}
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a travel advisor"},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            content = response.choices[0].message.content
            return content
        except Exception as e:
            # Handle error (logging, re-raising, etc.)
            return f"Error occurred: {str(e)}"


# Usage Example
if __name__ == "__main__":
    client = OpenAIClient()

    rules = """
    Give me an itinerary based on the following
    Add hotel stay as well.
    Generate an approximate final budget for the entire itinerary.
    If possible also give links to websites for booking.
    Just the itinerary, no explanation
    """

    destination = "Somewhere in Oceania"
    travel_type = "solo, adventurous"
    time = "sometime this December"

    result = client.get_itinerary(destination, travel_type, time, rules)
    print(result)
