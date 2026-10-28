from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="1337")

while True:
    user_input = input("You:\n")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    # Add stream=True parameter
    response = client.chat.completions.create(
        model="any",
        messages=[{"role": "user", "content": user_input}],
        stream=True,  # Enable streaming
        
    )
    
    # Handle streaming response
    print("Bot:\n", end="", flush=True)
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()  # Print newline after complete response