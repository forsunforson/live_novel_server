import anthropic

client = anthropic.Anthropic()

def claude_text_generator(system_role, text):
    return "hello_world"
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=5000,
        temperature=1,
        system=system_role,
        messages=text,
    )
    return str(message.content[0].text)

