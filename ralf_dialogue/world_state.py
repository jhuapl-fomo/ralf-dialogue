###############
##  Imports  ##
###############

# Standard lib
import json
import os
from pathlib import Path

# Ours
from ralf.dispatcher import Action, ActionDispatcher
import ralf.utils as utils


#############
## Globals ##
#############

_module_path = os.path.abspath(__file__)
_internal_ralf_path = Path(_module_path).parent / Path('ralf_data/')
DISPATCHER = ActionDispatcher(_internal_ralf_path)


#############
## Helpers ##
#############



##############################
##  Information Extraction  ##
##       Functions          ##
##############################

# Perhaps have separate state extractor class here
# it would be provided a list of relevant topics and
# mostly attend to extracted information relevant to those
#
# the worldstate class would be relegated to only an information passing
# class (subclassing dict) produced by by the extractor class, and
# able to intelligently update itself given a new worldstate dict


##################
##  Main Class  ##
##################

class WorldState(dict):
    def __init__(self, topics=None, path_to_init=None, **kwargs):
        self.topics = topics
        self.path_to_init = path_to_init

        if path_to_init is not None:
            init_dict = utils.load_yaml(path_to_init)
            kwargs.update(init_dict)

        super().__init__(**kwargs)

    def extract_state(self, conversation, num_turns_context=2):
        extracted_state = DISPATCHER(
            [Action(prompt_name='extract_world_state')],
            **{
                'conversation': conversation.to_list()[-num_turns_context:]
            }
        )['output']

        extracted_state = utils.str_to_dict_safe(extracted_state)

        return extracted_state

    def update(self, new_world_state):
        new_world_state = DISPATCHER(
            [Action(prompt_name='update_world_state')],
            **{
                'old_state_dict': json.dumps(self, indent=3),
                'new_state_dict': new_world_state
            }
        )['output']

        new_world_state = utils.str_to_dict_safe(new_world_state)

        self.clear()

        super().update(new_world_state)
