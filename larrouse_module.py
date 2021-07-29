import requests
import bs4
import re


def get_example_phrase(word):
    word = word.lower()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    res = requests.get(
        "https://www.larousse.fr/dictionnaires/francais/" + word, headers=headers
    )
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    soup_elements = soup.find_all("span", class_="ExempleDefinition")
    try:
        return str(soup_elements[0].getText())
    except:
        return None


def get_monolingual_translation(word):
    word = word.lower()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    res = requests.get(
        "https://www.larousse.fr/dictionnaires/francais/" + word, headers=headers
    )
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    soup_elements = soup.find_all("li", class_="DivisionDefinition")
    text_list = []
    trash_regex = re.compile(r"\xa0|\n|\t|\r")
    reducer_regex = re.compile(r"^.*?:")

    if len(soup_elements) > 0:
        for i in range(len(soup_elements)):
            try:
                temp_element = soup_elements[i].getText()
                temp_element = trash_regex.sub(" ", temp_element)
                mo = reducer_regex.search(temp_element)
                temp_element = mo.group()
                temp_element = temp_element[3:-1]
            except:
                pass

            text_list.append(temp_element)

        return text_list
    else:
        return None


def get_translation(word):
    word = word.lower()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    res = requests.get(
        "https://www.larousse.fr/dictionnaires/francais-anglais/" + word,
        headers=headers,
    )
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    soup_elements = soup.find_all("a", class_="lienarticle2")
    try:
        text_list = []
        if len(soup_elements) > 0:
            for i in range(len(soup_elements)):
                text_list.append(soup_elements[i].getText())

            return text_list
        else:
            return None
    except:
        return None


def get_reverse_translation(word):
    word = word.lower()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    res = requests.get(
        "https://www.larousse.fr/dictionnaires/anglais-francais/" + word,
        headers=headers,
    )
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    soup_elements = soup.find_all("a", class_="lienarticle2")
    text_list = []

    if len(soup_elements) > 0:
        for i in range(len(soup_elements)):
            text_list.append(soup_elements[i].getText())

        return text_list
    else:
        return None
