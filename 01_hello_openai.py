from openai import OpenAI;
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}
    ]
)

print(completion.choices[0].message.content)

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