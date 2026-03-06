TAMIL_GREETINGS = {
    "hello": "Vanakkam",
    "goodbye": "Poittu varen",
    "thank you": "Nandri",
    "good morning": "Kaalai vanakkam",
    "good evening": "Maalai vanakkam",
    "good night": "Iravu vanakkam",
    "how are you": "Eppadi irukkeenga",
    "welcome": "Varaverppu",
    "please": "Thayavu seithu",
    "sorry": "Mannikavum",
}


def translate(greeting):
    return TAMIL_GREETINGS.get(greeting.strip().lower())


def main():
    print("=== English to Tamil Greeting Translator ===")
    print(f"Supported greetings: {', '.join(TAMIL_GREETINGS.keys())}")
    print("Type 'list' to see all greetings, or 'quit' to exit.\n")

    while True:
        user_input = input("Enter a greeting in English: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye! / Poittu varen!")
            break
        elif user_input.lower() == "list":
            print("\nAll supported greetings:")
            for eng, tamil in TAMIL_GREETINGS.items():
                print(f"  {eng:20} -> {tamil}")
            print()
        else:
            result = translate(user_input)
            if result:
                print(f"  Tamil: {result}\n")
            else:
                print(f"  '{user_input}' not found. Type 'list' to see supported greetings.\n")


if __name__ == "__main__":
    main()