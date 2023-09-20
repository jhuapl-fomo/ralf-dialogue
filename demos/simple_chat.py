from ralf.dispatcher import Action
from ralf_dialogue import Conversation
from termcolor import colored


create_ai_response = Action(
    prompt_template="Below is a conversation between an AI and a human."
    "Complete the conversation by providing the AI's response."
    "{conversation_history}"
    "AI:"
)

conversation = Conversation()

while True:
    # Get input from the user and add it to the conversation
    user_utterance = input(colored('Human: ', 'blue', attrs=['bold']))
    if user_utterance == 'exit':
        break
    conversation.add_human_turn(user_utterance)

    # Generate the AI response using the current conversation history
    response = create_ai_response(context={'conversation_history': conversation})
    ai_utterance = response['output']

    # Add and display the AI turn
    ai_turn = conversation.add_ai_turn(ai_utterance, return_turn=True)
    print(f"{colored(ai_turn.speaker+':', 'green', attrs=['bold'])} {ai_turn.utterance}")