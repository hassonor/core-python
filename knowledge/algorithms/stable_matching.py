def stable_matching(men_preferences, women_preferences):
    # Initialize the couples dictionary as empty
    couples = {}

    # Initially, all women are free
    free_women = list(women_preferences.keys())

    while free_women:
        # Pick a free woman
        woman = free_women[0]

        # This woman checks the next man in her preference list that she hasn't yet been rejected by
        for man in women_preferences[woman]:
            # If the man is free
            if man not in couples:
                # They become a couple
                couples[man] = woman
                free_women.remove(woman)
                break
            # If the man is already paired with another woman
            else:
                current_woman = couples[man]
                # If the man prefers his current partner over the new woman
                if men_preferences[man].index(current_woman) < men_preferences[man].index(woman):
                    continue
                # If the man prefers the new woman
                else:
                    # The new woman becomes the man's partner
                    couples[man] = woman
                    free_women.remove(woman)
                    # The current woman becomes free
                    free_women.append(current_woman)
                    break

    return couples


if __name__ == "__main__":
    # Define men and women preferences
    men_preferences = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'Z', 'X'],
        'C': ['Z', 'X', 'Y']
    }

    women_preferences = {
        'X': ['B', 'A', 'C'],
        'Y': ['C', 'B', 'A'],
        'Z': ['A', 'C', 'B']
    }

    couples = stable_matching(men_preferences, women_preferences)
    # Print all couples
    for man, woman in couples.items():
        print(f'{man} is paired with {woman}')
