"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('When someone texts my number respond with "hello"',
                        '<Response><Message>Hello</Message></Response>'))
gpt.add_example(Example('When someone texts me respond asking who they are"',
                        '<Response><Message>Who are you?</Message></Response>'))
gpt.add_example(Example('When someone calls my number forward the call to +17187533087',
                        '<Response><Dial>+17187533087</Dial></Response>')),
gpt.add_example(Example('put everyone who calls this number into a conference call together',
                        '<Response><Dial><Conference>MyConferenceCall</Conference></Dial></Response>')),
gpt.add_example(Example('When someone calls this number say record this message and then record what they say',
                        '<Response><Say>Please record a message</Say><Record /></Response>')),
gpt.add_example(Example('reply back to any text message with i am groot', '<Response><Message>I Am Groot</Message><Response>')),
gpt.add_example(Example(
    'When someone calls my number ask them to say which department theyd like to talk to and collect what they say', '<Response><Say>Which departement would you like to talk to?</Say><Gather></Gather></Response>'))

# Define UI configuration
config = UIConfig(description="TwiML Generator",
                  button_text="Generate",
                  placeholder="TwiML Generator")

demo_web_app(gpt, config)
