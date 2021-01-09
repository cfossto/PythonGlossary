import random
from word import Word

class VocabularyTrainingProgram():

    word_list = []

    def show_main_menu(self):

        choice = 0

        while choice != 5:
            print("\n Chose an option: \n")
            print("1. Add a new word")
            print("2. Shuffle the wordlist")
            print("3. Take the test")
            print("4. Show all the words")
            print("5. Exit \n")

            choice = int(input())
            print()

            if choice == 1:
                self.add_new_word()
            elif choice == 2:
                self.shuffle_list()
            elif choice == 3:
                self.take_the_test()
            elif choice == 4:
                self.show_all_the_words()


        # Add if-clause to test number from choice
    

    def add_new_word(self):
        swe_word = input("Write a swedish word: ")
        en_word = input("Write an englist word: ")

        new_word = Word(swe_word,en_word)
        self.word_list.append(new_word)


    def show_all_the_words(self):
        for words in self.word_list:
            words.test()
            print()


    def shuffle_list(self):
        random.shuffle(self.word_list)

    def take_the_test(self):
        fails = 0
        MAX_FAILURES = 3

        for words in self.word_list:
            if fails == MAX_FAILURES:
                print("Game over. Practice more!")
                return False

            print("What is the English word for: "+ words.get_swedish_word())
            en_word = input()

            if words.verify_answer(en_word) == True:
                print("\nCorrect!")
            else:
                print("\nWrong, the correct answer is "+ words.get_english_word())
                fails += 1
        
        


VocabularyTrainingProgram().add_new_word()
VocabularyTrainingProgram().add_new_word()
VocabularyTrainingProgram().add_new_word()
VocabularyTrainingProgram().add_new_word()
VocabularyTrainingProgram().take_the_test()