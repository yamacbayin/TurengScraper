class Word:

    def __init__(self, english_word=None, turkish_equals_list=None, wrong_answer=None):
        self.english_word = english_word
        self.turkish_equals_list = turkish_equals_list
        self.wrong_answer = wrong_answer

    def __str__(self):
        return f"{self.english_word}, {self.turkish_equals_list}, {self.wrong_answer}."

    @staticmethod
    def check_and_populate_list_elements(scraped_list):
        """
            Checks the length of fetched Turkish words list.
            If it's lesser than 5, populates empty indexes with duplicates of existing words.
            Duplicates start from index 0 and increment the index by 1 if possible.
        """
        populated_list = []
        scraped_list_length = len(scraped_list)
        if scraped_list_length < 5:
            for i in range(5):
                index = i
                while index >= scraped_list_length:
                    index = index - scraped_list_length
                populated_list.append(scraped_list[index])
            return populated_list
        else:
            return scraped_list
