class Conditions:
    conditions = {
            'greater than': lambda player_attr, search_val: player_attr > search_val,
            'less than': lambda player_attr, search_val: player_attr < search_val,
            'not equal': lambda player_attr, search_val: player_attr != search_val,
        }
