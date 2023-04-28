from Word import Word
from DatabaseManager import DatabaseManager
from Scraper import Scraper


def main():
    dbm = DatabaseManager()
    scraper = Scraper()

    index = dbm.get_last_row_id()

    while index > 0:
        word = dbm.read_word(index)
        if word is None:
            break
        print("Read word: " + word.english_word + ", at index: " + str(index))
        results = scraper.fetch_result(word.english_word)
        word.turkish_equals_list = Word.check_and_populate_list_elements(results)
        dbm.write_word(word)
        print("Wrote word to database. " + word.__str__())
        index = index + 1

    scraper.close_driver()
    dbm.close_connection()


if __name__ == '__main__':
    main()
