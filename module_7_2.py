def custom_write(file_name, strings):

    with open(file_name, 'a', encoding='utf-8') as f:
        strings_positions = {}
        for i in range(len(strings)):
            inf = (i+1, f.tell())
            f.write(strings[i] + '\n')
            strings_positions[inf] = strings[i]
        return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)