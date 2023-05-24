from ralf import classifier


#######################
## Intent Classifier ##
#######################

class IntentClassifier:
    def __init__(
            self,
            intents: dict[str, list[str]]
    ):

        self.zs_classifier = classifier.ZeroShotClassifier()

        for intent, examples in intents.items():
            self.zs_classifier.add_class(
                intent,
                examples
            )

    def __call__(self, utterance) -> tuple[str, str]:
        return self.evaluate(utterance)

    def evaluate(self, utterance) -> tuple[str, str]:
        """
        Returns an index into the edge criteron list corresponding to the 
        predicted next edge
        """
        label, scores = self.zs_classifier(utterance)

        return label, scores
