import anthropic

client = anthropic.Anthropic()

def text_generator(text):
    # 这里可以添加具体的文本生成逻辑
    messages = [
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
    return claude_text_generator(system_define_poet, messages)


def multi_round_generator(json_data):
    messages = [
        {
            "role": "user",
            "content": [
                    {
                        "type": "text",
                        "text": """
To start the game:
Explain the game rules to me.
Let me choose a character from a list you provide, with a brief summary of each character's traits.
Once I have chosen, we can begin the game from the start of the script.
"""
                    }
            ]
        }
    ]
    for item in json_data['messages']:
        if item['role'] == 'user':
            messages.append({
                "role": "user",
                "content": [
                        {
                            "type": "text",
                            "text": item['content']
                        }
                ]
            })
        elif item['role'] == 'assistant':
            messages.append({
                "role": "assistant",
                "content": [
                        {
                            "type": "text",
                            "text": item['content']
                        }
                ]
            })

    return claude_text_generator(system_define_game_master % json_data['game'], messages)

system_define_poet = "You are a world-class poet. Respond only with short poems."
system_define_game_master = """Game Rules:
Let's play a text-based game of %s. I will play one of the characters, and you will narrate the storyline and play the other characters, guiding me through the plot framework. After each interaction or dialogue, we will move to the next part of the story.
In your responses, please pay attention to the following points:

Summarize the key plot points of the script and identify critical interaction nodes.
Before reaching an interaction event, you can recite the script content verbatim to ensure the original text's value, using the original descriptions and dialogues as much as possible.
Upon reaching an interaction node, you will provide interaction options from the character's perspective or as a narrator, allowing the user to select using letters. Each option should be related to foreshadowing in the text.
For possible non-original responses from the user, you need to flexibly adjust the subsequent storyline without disrupting the main plot.
The newly generated plot should not contain spoilers or excessive hints and should not introduce future characters or items from the script prematurely.
"""

def claude_text_generator(system_role, text):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=5000,
        temperature=1,
        system=system_role,
        messages=text,
    )
    print(message, end='', flush=True)
    for char in str(message):
        yield char

