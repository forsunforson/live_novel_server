import anthropic

def text_generator(text):
    # 这里可以添加具体的文本生成逻辑
    return claude_text_generator(text)

client = anthropic.Anthropic()

def claude_text_generator(text):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        temperature=1,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                        {
                            "type": "text",
                            "text": text
                        }
                ]
            }
        ]
    )
    
    for char in message.content[0].text:
        print(char, end='', flush=True)
        yield char
