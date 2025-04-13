import os
import requests
import re
from collections import Counter

def get_text(url, cache_file="cached_page.html"):
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return f.read()
    response = requests.get(url)
    text = response.text
    with open(cache_file, 'w', encoding='utf-8') as f:
        f.write(text)
    return text

def preprocess_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    raw_text = get_text(url)
    words = preprocess_text(raw_text)
    word_counter = Counter(words)

    with open(words_file, 'r') as file:
        words_to_count = [line.strip().lower() for line in file if line.strip()]

    frequencies = {word: word_counter[word] for word in words_to_count}

    print(frequencies)

if __name__ == "__main__":
    main()
