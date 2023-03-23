# Задание 4
# № 4

import file_parser


# Реализовать функции кодирования и декодирования текста циклическим сдвигом букв алфавита.
# Величина сдвига передается вторым параметром в данные функции.
# Например, если величина сдвига равна 2, то все буква А меняется В, Б – на Г, В – на Д, …, Ю – на А, Я – на Б.
# Такая же логика действует для замены латинских букв. Меняться должны как прописные, так и строчные буквы (при этом прописные буквы остаются прописными, а строчные – строчными).
# Подсказка: в программе в виде строковой константы должен быть задан русский и латинский алфавит и все манипуляции с текстом производятся работой с данной константой
# (ни в коем случае программа не должна содержать отдельные условные операторы для замены каждой буквы).

class Caesar_cipher_coder:
    d = {'RU': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'EU': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
         'JP': 'ンワラヤマハナタサカアリミヒニチシキイルユムフヌツスクウレメヘネテセケエヲロヨモホノトソコオ'}

    def choose_language(self, message):
        for el in message:
            for key in self.d:
                if el in self.d.get(key) or el in self.d.get(key).lower():
                    return self.d.get(key)
        return ''

    def cipher(self, language, source_message, rot):
        coded_message = ''
        for ch in source_message:
            if ch in language or ch in language.lower():
                if ch.isupper():
                    curr_ind = language.find(ch)
                    res_rot = (curr_ind + rot) % len(language)
                    next_ch = language[res_rot]
                else:
                    curr_ind = language.find(ch.upper())
                    res_rot = (curr_ind + rot) % len(language)
                    next_ch = language[res_rot].lower()
                coded_message += next_ch
            else:
                coded_message += ch
        return coded_message


def run_application(input_path, output_path, cipher_coder, rot):
    data = file_parser.read_str(input_path)
    result = cipher_coder.cipher(cipher_coder.choose_language(data), data, rot)
    file_parser.write_str_to_file(result, output_path)


cc = Caesar_cipher_coder()

run_application("files/input01.txt", "files/output01.txt", cc, 1)
run_application("files/input02.txt", "files/output02.txt", cc, 13)
run_application("files/input03.txt", "files/output03.txt", cc, 50)
run_application("files/input04.txt", "files/output04.txt", cc, 1)
run_application("files/input05.txt", "files/output05.txt", cc, 1)
