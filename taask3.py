import re

# Define a list of conversation patterns and responses
patterns_responses = [
    (r"my name is (.*)", "Hello {0}, how are you today?"),
    (r"hi|hey|hello", "Hello!"),
    (r"what is your name?", "I am a chatbot created by you. You can call me Chatbot."),
    (r"how are you?", "I'm doing good. How about you?"),
    (r"sorry (.*)", "It's alright, no problem at all."),
    (r"I am fine", "Great to hear that!"),
    (r"i'm (.*) doing good", "Nice to hear that!"),
    (r"what (.*) want ?", "Make me an offer I can't refuse."),
    (r"(.*) created ?", "I was created using Python by a developer."),
    (r"(.*) (location|city) ?", "I'm a virtual entity, but you can find me wherever you run my code!"),
    (r"how is the weather in (.*)?", "The weather in {0} is great! Just kidding, I don't have weather data."),
    (r"i work in (.*)?", "{0} is an interesting place to work!"),
    (r"quit", "Bye, take care. See you soon."),
    (r"(.*)", "I am not sure how to respond to that.")
]

# Function to match user input with patterns and generate responses
def match_pattern(user_input):
    for pattern, response in patterns_responses:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            return response.format(*match.groups())
    return "I am not sure how to respond to that."

# Define a function to start the chatbot
def chatbot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")  # Welcome message
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Bye, take care. See you soon.")
            break
        response = match_pattern(user_input)
        print(response)

if __name__ == "__main__":
    chatbot()
