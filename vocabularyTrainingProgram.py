import random
from word import Word

class VocabularyTrainingProgram():

    word_list = []
    highscore = 0
    highscore_list = []

    def show_main_menu(self):

        choice = 0

        while choice != 6:
            print("\n Chose an option: \n")
            print("1. Add a new word")
            print("2. Shuffle the wordlist")
            print("3. Take the test")
            print("4. Show all the words")
            print("5. Show high-score.")
            print("6. Exit \n")

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
            elif choice == 5:
                self.show_high_score()




    def add_new_word(self):
        swe_word = input("Write a swedish word: ").lower()
        en_word = input("Write an english word: ").lower

        new_word = Word(swe_word,en_word)
        self.word_list.append(new_word)


    def show_all_the_words(self):
        for words in self.word_list:
            words.test()
            print()


    def shuffle_list(self):
        random.shuffle(self.word_list)


    def show_high_score(self):
        print("Your greatest scores this session:")
        score_list = self.highscore_list
        score_list.sort()
        score_list.reverse()

        if len(score_list) < 5:
            for scores_index in range(0,len(score_list)):
                position = scores_index + 1
                print("{}: {} ".format(str(position),str(score_list[scores_index])))
        else:
            for scores_index in range(0,5):
                position = scores_index + 1
                print("{}: {} ".format(str(position),str(score_list[scores_index])))


    


    def take_the_test(self):
        fails = 0
        MAX_FAILURES = 3
        game = True
        tmp_high_score = 0

        while game == True:

            for words in self.word_list:
                if fails == MAX_FAILURES:
                    print("Game over. Practice more!")
                    return False

                print("What is the English word for: "+ words.get_swedish_word())
                en_word = input().lower

                if words.verify_answer(en_word) == True:
                    print("\nCorrect!")
                    self.highscore += 1
                else:
                    print("\nWrong, the correct answer is "+ words.get_english_word())
                    self.highscore -= 1
                    fails += 1

            print("Round completed. You got: "+ str(self.highscore))
            tmp_high_score += 1
            play_again = int(input("Select 1 to play again or 0 to quit. "))

            if play_again == 0:
                game = False
        
        self.highscore_list.append(tmp_high_score)
        return False
