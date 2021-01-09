class Word():

    swedish_word = ""
    english_word = ""

    def __init__(self,swedish_word,english_word):
        self.english_word = english_word
        self.swedish_word = swedish_word

    def test(self):
        print(self.swedish_word)
        print(self.english_word)

    def get_english_word(self):
        return self.english_word

    def get_swedish_word(self):
        return self.swedish_word

    def verify_answer(self,answer):
        if answer == self.english_word:
            return True
