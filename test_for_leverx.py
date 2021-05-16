import re


class TestCreator:
    NUM_OPTIONS = 4
    MINIMAL_RIGHT_ANSWERS = 1

    def __init__(self, function=None, alert=None):
        self._questions = []
        self._input = function if function else self._input
        self._alert = alert if alert else self._alert

        self.step_list = {
            "title": self._add_title,
            "options": self._add_option,
            "answers": self._add_answers,
        }

    def create_question(self):
        new_question = dict()

        for key in self.step_list:
            result = self.step_list[key]()
            if not result:
                break
            else:
                new_question[key] = result

        else:
            new_question["NUM_OPTIONS"] = self.NUM_OPTIONS
            new_question["MINIMAL_RIGHT_ANSWERS"] = self.MINIMAL_RIGHT_ANSWERS
            # print(new_question)
            self._questions.append(new_question)

    def _add_title(self):
        title = self._input("Введите текст вопроса: ")
        if self._is_correct(title):
            return title
        self._alert("Вы не ввели текст вопроса. Попробуйте добавить вопрос заново.")
        return False

    def _add_option(self):
        all_option = []
        for i in range(self.NUM_OPTIONS):
            option = self._input(f"Введите текст {i + 1} варианта ответа: ")
            if self._is_correct(option):
                all_option.append(option)
            else:
                self._alert(f"Вы не ввели текст {i + 1} варианта ответа. Попробуйте добавить вопрос заново.")
                return False
        return all_option

    def _add_answers(self):
        right_options = self._input(
            f"Введите номера правильных ответов через запятую. Нумерация начинается с {self.MINIMAL_RIGHT_ANSWERS}: ")
        checked_options = self._check_input_right_answers(right_options)
        if checked_options:
            return checked_options
        self._alert(
            f"Поле может содержать только уникальные цифры от {self.MINIMAL_RIGHT_ANSWERS} до {self.NUM_OPTIONS}"
            " разделенные запятой. Попробуйте добавить вопрос заново.")

    def _is_correct(self, string):
        result = string.strip()
        if result:
            return True
        return False

    def _check_input_right_answers(self, string):
        if type(string) == str:
            if not re.search(r"[^, \d]+", string):
                all_answers = re.findall(r"\d+", string)
                if (self.MINIMAL_RIGHT_ANSWERS <= len(all_answers) <= self.NUM_OPTIONS)\
                        and (len(set(all_answers)) == len(all_answers)):

                    result = [int(item) - 1 for item in re.findall(r"\d+", string) if
                              self.NUM_OPTIONS >= int(item) >= self.MINIMAL_RIGHT_ANSWERS]
                    return result

        return False

    def _input(self, title):
        return input(title)

    def _alert(self, message):
        print(message)


class Test(TestCreator):
    def __init__(self, questions=None, function=None, alert=None):
        TestCreator.__init__(self, function=function, alert=alert)
        self._questions = self._questions if self._questions else questions

    def start_test(self):
        if self._questions:
            user_answers = []
            true_answer = 0
            for number_question in range(len(self._questions)):
                question = self._questions[number_question]
                output_string = f"{number_question + 1}. {question['title']} \n"
                number = 1
                for option in question["options"]:
                    output_string += f"\t{number}. {option}\n"
                    number += 1
                self._alert(output_string)
                answer = self._check_input_right_answers(
                    self._input(f"Введите правильные варианты"
                                f" {self.MINIMAL_RIGHT_ANSWERS} до {self.NUM_OPTIONS} через запятую: "))

                if answer:
                    if answer == question["answers"]:
                        user_answers.append(True)
                        true_answer += 1
                    else:
                        user_answers.append(False)
                else:
                    self._alert(f"Вы преравали тестирование на {len(user_answers) + 1} вопросе.")
                    break
            if len(self._questions) == true_answer:
                self._alert(f"Ваш результат {true_answer} из {len(self._questions)}. Вы молодец!")

            elif user_answers.count(False):
                output_string = "Вы неправильно ответили на вопросы:\n"
                for i in range(len(user_answers)):
                    if user_answers[i] == False:
                        output_string += f"{i + 1}. {self._questions[i]['title']}\n"
                output_string += f"Ваш результат {true_answer} из {len(self._questions)}"
                self._alert(output_string)


        else:
            self._alert("Тест пуст")


if __name__ == '__main__':
    question1 = {
        "title": "Что из перечисленного не является языком программирования?",
        "options": [
            "HTML",
            "Java",
            "Python ",
            "DevOps",
        ],
        "answers": [0, 3]
    }

    question2 = {
        "title": "Какие из перечисленных видов тестирования могу быть автоматизированы?",
        "options": [
            "UI тестирование",
            "Юзабилити тестирование",
            "Тестирование совместимости",
            "Unit тестирование",
        ],
        "answers": [0, 2, 3]
    }

    question3 = {
        "title": 'Выберите вариант, который соответствует следующему предложению: "Известно, что ' +
                 'грымзик обязательно или полосат, или рогат, или то и другое"',
        "options": [
            "Грымзик не может быть безрогим",
            "Грымзик не может быть однотонным и безрогим одновременно",
            "Грымзик не может быть полосатым и безрогим одновременно",
            "Грымзик не может быть однотонным и рогатым одновременно",
        ],
        "answers": [1]
    }

    question4 = {
        "title": "Выбирите типы алгоритмов, которых не существует:",
        "options": [
            "Алгоритм с ветвлением",
            "Циклический безусловных",
            "Циклический с параметрами",
            "Алгоритм с углублением",
        ],
        "answers": [1, 3]
    }

    question5 = {
        "title": "Какого (каких) метода (методов) тестирования не существует?",
        "options": [
            "Метод белого ящика",
            'Метод "игры в ящик"',
            'Метод "кротовой норы"',
            "Метод серого ящика",
        ],
        "answers": [1, 2]
    }

a = Test([question1, question2, question3, question4, question5])
a.create_question()
a.start_test()
