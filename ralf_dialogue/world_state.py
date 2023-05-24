class WorldState(dict):
    def __init__(self, topics=None, **kwargs):
        super().__init__(**kwargs)

    def update(self, conversation):
        pass
