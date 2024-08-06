class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for f in self.file_names:
            with open(f, 'r', encoding='utf-8') as file:
                words = file.read().split()
                all_words[f] = words
        self.toResult(all_words)
        return all_words

    def find_(self, word):
        find_vocab = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for f, words in all_words.items():
            try:
                pos = words.index(word)  # Ищем первое вхождение слова в списке
            except ValueError:
                pos = -1  # Если слово не найдено, устанавливаем -1
            find_vocab[f] = pos+1 # чтобы нумероват ьне с нуля
        self.toResult(find_vocab)
        return find_vocab

    def count(self, word):
        find_count = {}
        all_words = self.get_all_words()
        for f, words in all_words.items():
            cnt = 0
            for w in words:
                if w == word:
                    cnt += 1
            find_count[f] = cnt
        self.toResult(find_count)
        return find_count

    def toResult(self, txts): # сохраняем полученные результаты в файл
        with open('itog.txt', 'a', encoding='utf-8') as file:
            for key, value in txts.items():
                file.write(f'{key}: {value}\n')

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')

myWord = 'the'
f1 = WordsFinder('text_.txt')
print(f1.get_all_words())
print(f1.find_('text'))
print(f1.count('text'))
print('====== поиск слова "the" в файле "text_.txt" ========')
print(f1.find_('text'))
print(f1.count('text'))

print('====== поиск и подсчет слова "the" в нескольких файлах ========')
print(f'Тексты из файлов в строку: {finder1.get_all_words()}')
print(f'в файлах первое вхождение слова "{myWord}" приходится на слово с номером {finder1.find_(myWord)}')
print(f'в файлах количество встретившихся слов "{myWord}" равно {finder1.count(myWord)}')
print(f'П р и м е ч а н и е: полученные данные сохранены в файл "itog.txt"')

