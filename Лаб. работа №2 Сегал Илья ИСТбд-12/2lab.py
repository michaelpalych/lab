import re

DIGIT_WORDS = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

def number_to_words(number: str) -> str:
    return ' '.join(DIGIT_WORDS[digit] for digit in number)

def process_file(filename: str):
    with open(filename, 'r') as file:
        content = file.read()
    
    numbers = re.findall(r'\b\d{1,5}\b', content)
    numbers = [num for num in numbers if int(num) % 2 == 0]
    
    for i, num in enumerate(numbers):
        print(number_to_words(num) if i % 2 == 0 else num)

process_file("2lab.txt")
