# Copyright (c) 2023 The Johns Hopkins University Applied Physics Laboratory

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
        Action(prompt_name='precisify_utterance2'),
        context={'conversation_text' : str(conversation)}  
    )['output']
    

    return disambiguated_utterance