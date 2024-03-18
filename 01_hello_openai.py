from openai import OpenAI
import json

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role" : "user",
            "content" : "what can u help me?"
        }
    ],
    temperature=0.7
)

print(json.dumps(json.loads(response.model_dump_json()), indent=4))

# {
#     "id": "chatcmpl-93kZOWeKTvv7Da8MYmtVsin05LDAu",
#     "choices": [
#         {
#             "finish_reason": "stop",
#             "index": 0,
#             "logprobs": null,
#             "message": {
#                 "content": "Arrr, me hearties, listen up ye scallywags! Asynchronous programming be like havin' a crew of pirates workin' on different tasks at the same time. Each pirate be doin' their own job, but they be communicatin' with the captain through messages in bottles. This way, the ship can be sailin' smoothly without all the pirates waitin' around for one task to be finished before movin' on to the next. So, me mateys, asynchronous programming be all about multitaskin' and keepin' the ship runnin' smoothly on the high seas of code! Arrr!",
#                 "role": "assistant",
#                 "function_call": null,
#                 "tool_calls": null
#             }
#         }
#     ],
#     "created": 1710681026,
#     "model": "gpt-3.5-turbo-0125",
#     "object": "chat.completion",
#     "system_fingerprint": "fp_4f2ebda25a",
#     "usage": {
#         "completion_tokens": 131,
#         "prompt_tokens": 21,
#         "total_tokens": 152
#     }
# }

# this is result
# Oh, wanderer in the realm of code,
# Let me weave a tale to lighten your load,
# Of objects and classes, a dynamic duo,
# In the dance of OOP, they steal the show.

# Imagine a class as a blueprint grand,
# Defining the structure of objects in hand,
# With attributes and methods, a treasure trove,
# To breathe life into instances that rove.

# And behold the objects, unique and divine,
# Instances of class, in orderly line,
# Each holding data, each with a spark,
# Ready to dance to the tune of the dark.

# Inheritance whispers a tale of old,
# Passing down traits, a legacy bold,
# Parent and child in a bond so tight,
# Sharing knowledge, like day and night.

# Polymorphism, a shape-shifting art,
# Objects morphing at will, playing their part,
# A method called here, a method called there,
# Adapting like chameleons with utmost care.

# Encapsulation, a secret well-kept,
# Data hidden away, safely kept,
# Only through methods can one peek inside,
# A fortress of privacy, a coder's pride.

# So embrace the objects, in classes nested,
# In the realm of OOP, where they’re tested,
# For in this world of code and lore,
# Objects and classes reign forevermore