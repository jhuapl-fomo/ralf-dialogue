class Turn:
    def __init__(self, speaker, utterance):
        self.speaker = speaker
        self.utterance = utterance

    def __str__(self):
        return f"{self.speaker}: {self.utterance}"

    def __repr__(self):
        return self.__str__()

class Conversation():
    def __init__(
            self,
            history=None,
            ai_attribution='AI',
            human_attribution='Human'
    ):

        self.history = history if history else []
        self.ai_attribution = ai_attribution
        self.human_attribution = human_attribution

    def add(self, speaker, utterance):
        self.history.append(Turn(speaker, utterance))

    def get_last_user_turn(self):
        for turn in reversed(self.history):
            if turn.speaker == self.human_attribution:
                return turn

    def to_list(self):
        return [str(turn) for turn in self.history]

    def __str__(self):
        result = []

        for turn in self.history:
            result.append(str(turn))

        return '\n'.join(result)

    def to_str_double_newline(self):
        result = []

        for turn in self.history:
            result.append(str(turn))

        return '\n\n'.join(result)

    def __repr__(self):
        return self.__str__()
