from ralf.dispatcher import Action
from ralf_dialogue import Conversation
from termcolor import colored

# Create the conversation object
conversation = Conversation()

# Provide a system message that will dictate the assistant's behavior
system_msg = "You are a helpful assistant that speaks with a pirate accent."

while True:
    # Get input from the user and add it to the conversation
    user_utterance = input(colored('Human: ', 'blue', attrs=['bold']))
    if user_utterance == 'exit':
        break
    conversation.add_human_turn(user_utterance)

    # Generate the AI response using the current conversation history
    response = Action(messages=conversation.to_messages(system_msg))()
    ai_utterance = response['output']

    # Add and display the AI turn
    ai_turn = conversation.add_ai_turn(ai_utterance, return_turn=True)
    print(f"{colored(ai_turn.speaker+':', 'green', attrs=['bold'])} {ai_turn.utterance}")