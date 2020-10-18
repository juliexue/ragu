from enum import Enum
from typing import Optional


class ShowPointsSetting(Enum):
    ALL = 'all'
    SHOW_STOLEN_POINTS_ONLY = 'show_stolen_points_only'
    NONE = 'none'


class GameSettingsBuilder(object):
    def __init__(self):
        self.game_settings = GameSettings()
        self.default_fields = {
            'num_decks', 'num_friends', 'max_stolen_points', 'stolen_points_for_promo', 'multi_promo_step_size',
        }

    def set_num_decks(self, num_decks: Optional[int]):
        if not num_decks:
            self.default_fields.add('num_decks')
        else:
            self.game_settings.num_decks = num_decks
            self.default_fields.remove('num_decks')
        return self

    def set_num_friends(self, num_friends: Optional[int]):
        if not num_friends:
            self.default_fields.add('num_friends')
        else:
            self.game_settings.num_friends = num_friends
            self.default_fields.remove('num_friends')
        return self

    def set_max_stolen_points(self, max_stolen_points: Optional[int]):
        if not max_stolen_points:
            self.default_fields.add('max_stolen_points')
        else:
            self.game_settings.max_stolen_points = max_stolen_points
            self.default_fields.remove('max_stolen_points')
        return self

    def set_stolen_points_for_promo(self, stolen_points_for_promo: Optional[int]):
        if stolen_points_for_promo:
            self.default_fields.add('stolen_points_for_promo')
        else:
            self.game_settings.stolen_points_for_promo = stolen_points_for_promo
            self.default_fields.remove('stolen_points_for_promo')
        return self

    def set_multi_promo_step_size(self, multi_promo_step_size: Optional[int]):
        if multi_promo_step_size:
            self.default_fields.add('multi_promo_step_size')
        else:
            self.game_settings.multi_promo_step_size = multi_promo_step_size
            self.default_fields.remove('multi_promo_step_size')
        return self

    def set_allow_takebacks(self, allow_takebacks: bool):
        self.game_settings.allow_takebacks = allow_takebacks
        return self

    def set_show_cards_played(self, show_cards_played: bool):
        self.game_settings.show_cards_played = show_cards_played
        return self

    def set_show_points(self, show_points: ShowPointsSetting):
        self.game_settings.show_points = show_points
        return self

    def set_incorrect_throw_penalty(self, incorrect_throw_penalty: int):
        self.game_settings.incorrect_throw_penalty = incorrect_throw_penalty
        return self

    def set_allow_bid_takeback(self, allow_bid_takeback: bool):
        self.game_settings.allow_bid_takeback = allow_bid_takeback
        return self

    def build(self):
        return self.game_settings


class GameSettings(object):
    def __init__(self):
        self.num_decks = None
        self.num_friends = None
        self.max_stolen_points = None
        self.stolen_points_for_promo = None
        self.multi_promo_step_size = None
        self.allow_takebacks = True
        self.show_cards_played = True
        self.show_points = ShowPointsSetting.ALL
        self.incorrect_throw_penalty = 0
        self.allow_bid_takeback = True
