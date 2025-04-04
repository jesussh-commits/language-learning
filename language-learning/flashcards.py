import random

# A dictionary of German words and their English translations
flashcards = {
    'Hund': 'dog',
    'Katze': 'cat',
    'Haus': 'house',
    'Buch': 'book',
    'Auto': 'car'
}

# Function to test user knowledge
def test_flashcards():
    print("Welcome to the German Flashcard Quiz!")
    score = 0
    total = len(flashcards)

    # Shuffle the flashcards for randomness
    words = list(flashcards.keys())
    random.shuffle(words)

    for word in words:
        translation = flashcards[word]
        answer = input(f"What is the English translation of '{word}'? ").strip()

        if answer.lower() == translation.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{translation}'.")
        
    print(f"\nYour final score is {score}/{total}")

# Run the flashcard test
if __name__ == "__main__":
    test_flashcards()

