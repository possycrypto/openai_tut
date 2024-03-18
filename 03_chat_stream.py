from openai import  OpenAI

client=OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What can u help me"}],
    stream=True,
)


for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="!")
        
# !I! can! assist! you! with! a! variety! of! things! such! as! answering! questions!,! providing! information!,! offering! suggestions! or! recommendations!,! giving! advice!,! helping! you! brainstorm! ideas!,! etc!.! Just! let! me! know! what! you! need! help! with! and! I! will! do! my! best! to! assist! you!.!