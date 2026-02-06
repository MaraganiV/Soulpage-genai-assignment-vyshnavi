import wikipedia

conversation_memory = []

print("Simple Knowledge Bot started")
print("Ask questions. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Session ended")
        break

    conversation_memory.append(user_input)

    try:
        result = wikipedia.summary(user_input, sentences=2)
        print("Bot:", result)
    except:
        if len(conversation_memory) > 1:
            try:
                context_query = conversation_memory[-2] + " " + user_input
                result = wikipedia.summary(context_query, sentences=2)
                print("Bot:", result)
            except:
                print("Bot: I could not find information.")
        else:
            print("Bot: I could not find information.")