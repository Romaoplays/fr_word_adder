import csv
import os

# import time

from larrouse_module import get_monolingual_translation
from larrouse_module import get_example_phrase
from larrouse_module import get_reverse_translation
from larrouse_module import get_translation

# Creates csv file if it doesn't exist
try:
    csv_file = open("fr_words.csv", encoding="utf-8-sig")
except FileNotFoundError:
    csv_file = open("fr_words.csv", "w", encoding="utf-8-sig")
finally:
    csv_file.close()


def add_to_csv(word):
    words_list = []
    words_list.append(word)
    print("...Word added")
    words_list.append(get_monolingual_translation(word)[0])
    print("...Monolingual added")
    # time.sleep(1)
    words_list.append(get_example_phrase(word))
    print("...Example phrase added")
    # time.sleep(1)
    words_list.append(get_translation(word)[0])
    print("...Translation added")

    csv_file = open("fr_words.csv", "a", encoding="utf-8-sig")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(words_list)
    csv_file.close()
    print("\n!!!Done!!!")


while True:
    print("\nWhat to do?\n1 - Define\n2 - Reverse Translate \n3 - View words")
    resposta = input()
    if resposta == "1":
        print("\nType out word:")
        resposta_palavra_portugues = input()
        current_word = get_monolingual_translation(resposta_palavra_portugues)
        if current_word is not None:
            for i in range(len(current_word)):
                if i < 3:
                    print(f"\nDefinition #{i+1}: \n{current_word[i]}")

            frase_exemplo = get_example_phrase(resposta_palavra_portugues)
            if frase_exemplo is not None:
                print(f"\n\n## Example phrase - {frase_exemplo}")

            print("\nWhat to do?\n1 - Add word\n2 - Translate\n3 - Quit")
            resposta = input()
            if resposta == "1":
                add_to_csv(resposta_palavra_portugues)
            if resposta == "2":
                translated_word = get_translation(resposta_palavra_portugues)
                for i in range(len(current_word)):
                    if i < 5:
                        print(f"\n\Translation #{i+1}: \n{current_word[i]}")
                print("\nWhat to do?\n 1 - Add word\n2 - Quit")
                resposta = input()
                if resposta == "1":
                    add_to_csv(resposta_palavra_portugues)
        else:
            print("\n!!!Translation not found!!!")
    if resposta == "2":
        print("\nType out word:")
        resposta_palavra_ingles = input()
        current_word = get_reverse_translation(resposta_palavra_ingles)
        if current_word is not None:
            for i in range(len(current_word)):
                if i < 3:
                    print(f"\nTranslation #{i+1}: \n{current_word[i]}")

        else:
            print("\n!!!Translation not found!!!")
    if resposta == "3":
        csv_file = open("fr_words.csv", "r", encoding="utf-8-sig")
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)

        csv_list_cleaner = []
        for row in csv_list:
            if row != []:
                csv_list_cleaner.append(row)

        csv_list = csv_list_cleaner

        k = 0

        print("Saved words:\n")
        for i in range(len(csv_list)):
            try:
                print(f"W: {csv_list[i][0]}  T: {csv_list[i][1]} || {csv_list[i][2]}")
            except IndexError:
                print(f"W: {csv_list[i][0]}  T: {csv_list[i][1]}")

        print(f"Total: {len(csv_list)} words")

        while True:
            print("\n'exit','ok','del' ")
            resposta_viewer = input()
            if resposta_viewer == "exit":
                csv_file.close()
                break
            elif resposta_viewer == "del":
                csv_file.close()
                os.remove("fr_words.csv")
                print("\nThe file has been cleared!")
                csv_file = open("fr_words.csv", "w", encoding="utf-8-sig")
                csv_file.close()
                break
            elif resposta_viewer == "ok":
                print("")
                for i in range(len(csv_list)):
                    if i <= k:
                        try:
                            print(
                                f"W: {csv_list[i][0]}  T: {csv_list[i][1]} || {csv_list[i][2]} ======= OK"
                            )
                        except IndexError:
                            print(
                                f"W: {csv_list[i][0]}  T: {csv_list[i][1]} ======= OK"
                            )
                    else:
                        try:
                            print(
                                f"W: {csv_list[i][0]}  T: {csv_list[i][1]} || {csv_list[i][2]}"
                            )
                        except IndexError:
                            print(f"W: {csv_list[i][0]}  T: {csv_list[i][1]}")
                k = k + 1