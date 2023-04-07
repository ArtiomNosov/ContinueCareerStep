# филиал предприятия
enterprise_branch = [ "Москва",
                      "Ангарск",
                      "Владимир",
                      "Глазов",
                      "Зеленогорск",
                      "Ковров",
                      "Нижний Новгород",
                      "Новосибирск",
                      "Новоуральск",
                      "Подольск",
                      "Санкт-Петербург",
                      "Саров",
                      "Северск",
                      "Электросталь"]
# грейд
grade = [ "Стажер",
          "Младший специалист",
          "Специалист",
          "Старший специалист",
          "Ведущий специалист",
          "Эксперт",
          "Старший эксперт",
          "Ведущий эксперт",
          "Архитектор"]
# название должности
job_title = ["Специалист",
             "верстальщик"]
# технологии, используемые в работе
technologies = ["php",
                "Bitrix",
                "Vue.JS",
                "TypeScript",
                "Vuex",
                "SASS/LESS",
                "Javascript(ES6+)",
                "HTML5",
                "CCS3",
                "Scrum/Agile",
                "автоматизация тестирования",
                "Windows/Linux",
                "архитектура вычислительных систем",
                "информационная безопасность web-ресурсов",
                "системы управления базами данных",
                "cетевые протоколы",
                "web-технологии"]
first_name = ["Иван"]
second_name = ["Иванов"]
father_name = ["Иванович"]

input_1 = ["Иванов Иван Иванович", "Москва", "эксперт", "верстальщик"]

def to_lower(str_list):
  return [x.lower() for x in str_list]

enterprise_branch_lower = to_lower(enterprise_branch)
grade_lower = to_lower(grade)
job_title_lower = to_lower(job_title)
technologies_lower = to_lower(technologies)
input_lower = to_lower(input)
first_name_lower = to_lower(first_name)
second_name_lower = to_lower(second_name)
father_name_lower = to_lower(father_name)
job_title_lower

unknown_input = [x for x in input_lower if x not in enterprise_branch_lower and x not in grade_lower and x not in job_title_lower and x not in technologies_lower]
unknown_input

# поиск фио, берёт первое попавшееся
name_index = []
name = -1
for name in first_name_lower:
  for i in range(len(unknown_input)):
    if name in unknown_input[i]:
      name_index += [i]

if len(name_index) >= 1:
  name = unknown_input[name_index[0]]
else:
  print("Error name_index not found")

name

unknown_input_without_name = [unknown_input[i] for i in range(len(unknown_input)) if i not in name_index]
unknown_input_without_name

if len(unknown_input_without_name) == 0:
  print("OK")
else:
  print("Ошибка! Остались не распознанные аргументы: ")
  print(unknown_input_without_name)

# филиал предприятия введённые
enterprise_branch_input = [x for x in input_lower if x in enterprise_branch_lower]
# грейд введённый
grade_input = [x for x in input_lower if x in grade_lower]
# название должности введённое
job_title_input = [x for x in input_lower if x in job_title_lower]
# технологии, используемые в работе введённое
technologies_input = [x for x in input_lower if x in technologies_lower]

print("Вы ввели")
print(f"Филиал предприятия: {enterprise_branch_input}")
print(f"Грейд: {grade_input}")
print(f"Название должности: {job_title_input}")
print(f"Технологии: {technologies_input}")
print(f"Имя: {name}")
print(f"Неопределено: {unknown_input_without_name}")

input_types = []
for i in range(len(input_lower)):
  x = input_lower[i]
  if x in enterprise_branch_lower:
    input_types += ["филиал предприятия"]
  elif x in grade_lower:
    input_types += ["грейд"]
  elif x in job_title_lower:
    input_types += ["название должности"]
  elif x in technologies_lower:
    input_types += ["технологии"]
  else:
    input_types += ["NaN"]

input_types[name_index[0]] = "имя"
input_types

if "имя" not in input_types:
  print("Ошибка вы не ввели имя работника!")
if "филиал предприятия" not in input_types:
  print("Ошибка вы не ввели филиал предприятия!")
if "грейд" not in input_types:
  print("Ошибка вы не ввели грейд работника!")
if "название должности" not in input_types:
  print("Ошибка вы не ввели название должности!")

def process_input(input):
    return