import random

# List of 78 tarot cards (22 Major Arcana and 56 Minor Arcana cards)
tarot_cards = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "The Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World"
]

def draw(x):
    # Create a list to store the drawn cards
    drawn_cards = []

    # Draw x number of cards
    for _ in range(x):
        # Get a random index from the list of tarot cards
        index = random.randint(0, len(tarot_cards) - 1)
        # Append the corresponding card to the drawn_cards list
        drawn_cards.append(tarot_cards[index])

    # Return the drawn cards as a list of strings
    return drawn_cards

