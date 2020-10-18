class Game(object):
    def __init__(self, num_players: int, config=None):
        self.num_players = num_players
        self.config = config or self._get_default_config()

    def _get_default_config(self):
        return {}
