

class Main(object):

    def __init__(self, text):
        self.text = Text(text)
        self.words = []
        self.longest_word = None
        self.start_with = None
        self.end_with = None

    def find_all_words_that(self, start_with, end_with):
        self.start_with = start_with
        self.end_with = end_with

        for sentence in self.text.text:
            for word in sentence.sentence:
                if isinstance(word, Word) and word.word[0] == start_with and word.word[-1] == end_with:
                    self.words.append(word)

    def find_longest_word(self):
        if len(self.words) == 0:
            print("К сожелению, такого слова в тексте нет.")
        else:
            if len(self.words) == 1:
                self.longest_word = self.words[0]
            else:
                self.longest_word = sorted(self.words, key=lambda word: word.len)[-1]
            print(f'Самое длинное слово которое начинается на "{self.start_with}" и заканчивается на "{self.end_with}":'
                  f' "{self.longest_word}", количество бук в слове ({self.longest_word.len})', )


class Word:
    def __init__(self, word):
        self.word = list(word)
        self.len = len(word)

    def __repr__(self):
        return f"Word({''.join(self.word)})"


class Sentence:
    def __init__(self, sentence):
        sentence = re.findall(r"[\w']+|[.,!?;]", sentence)
        self.sentence = []
        for member in sentence:
            if member not in ".,!?;":
                member = Word(member)
            self.sentence.append(member)

    def __repr__(self):
        return f"Sentence{[self.sentence]}"


class Text:
    def __init__(self, text):
        text = text.split('.')
        self.text = []
        for sentence in text:
            self.text.append(Sentence(sentence))

    def __repr__(self):
        text = "Text("
        for sentence in self.text:
            text += f"{sentence}\n"
        text += ")"
        return text


if __name__ == "__main__":
    default = "Соображения высшего  порядка, а также повышение уровня\n " \
             "гражданского сознания напрямую зависит от экономической целесообразности принимаемых решений.\n" \
             " Разнообразный и богатый опыт курс на социально-ориентированный национальный проект требует от нас\n" \
             " системного анализа соответствующих условий активизации? Значимость этих проблем настолько очевидна,\n" \
             " что постоянный количественный рост и сфера нашей активности создаёт предпосылки качественно новых\n" \
             " шагов для позиций, занимаемых участниками в отношении поставленных задач. Задача организации,\n " \
             "в особенности же новая модель организационной деятельности обеспечивает широкому кругу \n" \
             " специалистов участие в формировании позиций, занимаемых участниками в отношении поставленных задач.\n" \
             " С другой стороны консультация с профессионалами из IT напрямую зависит от новых предложений.\n" \
             " Задача организации, в особенности же дальнейшее развитие различных форм деятельности обеспечивает\n" \
             " актуальность экономической целесообразности принимаемых решений! Задача организации, в особенности\n" \
             " же рамки и место обучения кадров создаёт предпосылки качественно новых шагов для ключевых\n" \
             " компонентов планируемого обновления. Соображения высшего порядка, а также постоянное\n " \
             "информационно-техническое обеспечение нашей деятельности играет важную роль в формировании\n " \
             "дальнейших направлений развитая системы массового участия.\n"
    print("Текст:\n", default)
    start = input("Введите первую букву:")
    end = input("Введите последнюю букву:")
    myLab = Main(default)
    myLab.find_all_words_that(start_with=start, end_with=end)
    myLab.find_longest_word()
