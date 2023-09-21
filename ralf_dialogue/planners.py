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

from ralf import classifier
import numpy as np

#######################
## Intent Classifier ##
#######################

class IntentClassifier:
    """
    A classifier for identifying intents in natural language utterances.
    Currently just a thin wrapper around a ZeroShotClassifier.

    :param intents: A dictionary where keys are intent labels, and values are 
        lists of example utterances for each intent.
    :type intents: dict[str, list[str]]
    """

    def __init__(
            self,
            intents: dict[str, list[str]]
    ):
        self.zs_classifier = classifier.ZeroShotClassifier()

        for intent, examples in intents.items():
            self.zs_classifier.add_class(intent, examples)

    def __call__(self, utterance: str) -> tuple[str, np.ndarray]:
        """
        Evaluates an utterance and returns the intent label and confidence scores.

        :param utterance: The input utterance to be classified.
        :type utterance: str

        :return: A tuple containing the classified intent label and an array of 
            confidence scores of each intent (Note: these come from a similarity
            computation between text emitted by the generative language model
            and the class labels, and thus do not quantify the confidence of the
            generative model on this particular task).
        :rtype: tuple[str, ndarray]
        """

        return self.evaluate(utterance)

    def evaluate(self, utterance: str) -> tuple[str, np.ndarray]:
        """
        Evaluates an utterance and returns the intent label and confidence scores.

        :param utterance: The input utterance to be classified.
        :type utterance: str

        :return: A tuple containing the classified intent label and an array of 
            confidence scores of each intent (Note: these come from a similarity
            computation between text emitted by the generative language model
            and the class labels, and thus do not quantify the confidence of the
            generative model on this particular task).
        :rtype: tuple[str, ndarray]
        """

        label, scores = self.zs_classifier(utterance)

        return label, scores
