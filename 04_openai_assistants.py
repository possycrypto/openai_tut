import time

import openai

client = openai.OpenAI()

# Create an assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="you are my personal math tutor, Write and run code to answer my question",
    tools=[{"type":"code_interpreter"}],
    model="gpt-3.5-turbo",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role="user",
    content="Solve the problem: 'x^2 + 5x + 6 = 0'. What is the value of x?"
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="solve the problem: x"
)

print("Checking Assistance Status")

while True:
  run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

  if run.status == "completed":
    print("done!")
    messages = client.beta.threads.messages.list(thread_id=thread.id)

    print("messages")
    for message in messages:
      assert message.content[0].type == "text"
      print({"role" : message.role, "message" : message.content[0].text.value})

    client.beta.assistants.delete(assistant.id)

    break
  else:
    print("in progress ...")
    time.sleep(2)