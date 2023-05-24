import os
from pathlib import Path

from ralf.dispatcher import ActionDispatcher, Action

# Create a dispatcher for ralf to use internally (TODO: move this?)
ralf_dir = Path(__file__).parent / 'ralf_data'
ad = ActionDispatcher(dir=ralf_dir)

def disambiguate(conversation): 

    # TODO: modify this call once single action execution is changed to allow
    # kwargs context
    disambiguated_utterance = ad.execute(
        Action(prompt_name='precisify_utterance'),
        context={'conversation_text' : str(conversation)}  
    )['output']
    

    return disambiguated_utterance