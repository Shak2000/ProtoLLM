import os
import random


class ProtoLLM:
    def __init__(self):
        self.word_map = dict()

    def train(self, text):
        word_list = text.split()

        for i in range(len(word_list) - 1):
            if word_list[i] not in self.word_map.keys():
                self.word_map[word_list[i]] = dict()
                self.word_map[word_list[i]]["Grand Total"] = 0
            if word_list[i + 1] not in self.word_map[word_list[i]]:
                self.word_map[word_list[i]][word_list[i + 1]] = 0

            self.word_map[word_list[i]][word_list[i + 1]] += 1
            self.word_map[word_list[i]]["Grand Total"] += 1

        self.word_map[word_list[-1]] = dict()

    def next_word(self, curr_word):
        if curr_word not in self.word_map.keys():
            return random.choice(list(self.word_map.keys()))

        index = random.randint(0, self.word_map[curr_word]["Grand Total"] - 1)
        track = 0
        for word in self.word_map[curr_word].keys():
            if word != "Grand Total":
                track += self.word_map[curr_word][word]
                if track > index:
                    return word
        return ""

    def end_of_sentence(self, word):
        return len(word) > 0 and (word[-1] == "." or word[-1] == "!" or word[-1] == "?")

    def gen_word_list(self, word_list, energy=0.8):
        start_len = len(word_list)
        while True:
            if self.end_of_sentence(word_list[-1]) and len(word_list) > start_len and random.random() > energy:
                break
            word_list.append(self.next_word(word_list[-1]))
        return word_list

    def gen_message(self, message, energy=0.8):
        word_list = self.gen_word_list(message.split(), energy)
        message = ""
        for i in range(len(word_list) - 1):
            message += word_list[i] + " "
        return message + word_list[-1]


def main():
    print("Welcome to the Proto-LLM app!")
    llm = ProtoLLM()

    while True:
        print()
        choice = input("Would you like to (1) enter a training file, (2) query a prompt, or (3) quit the program? ")

        if choice == "1":
            file_name = input("Please enter a training file: ")
            if os.path.exists(file_name):
                file = open(file_name, "r+")
                llm.train(file.read())
                print(f"Thank you for letting the Proto-LLM train on {file_name}!")
            else:
                print(f"{file_name} does not exist. Please try again.")

        elif choice == "2":
            energy = 0.8

            try:
                energy = float(input("Please enter a number from 0 to 9 indicating how talkative you want the Proto-LLM to be: ")) / 10.0
                if energy < 0:
                    energy = 0
                elif energy > 0.9:
                    energy = 0.9

            except ValueError as e:
                print("")

            prompt = input("Please enter a prompt: ")
            print("The Proto-LLM is thinking...")
            print(llm.gen_message(prompt, energy))

        elif choice == "3":
            break

        else:
            print(f"{choice} is not a valid input. Please try again.")


if __name__ == "__main__":
    main()
