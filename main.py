import numpy as np
import docx


def is_active_rule(first_rule_part, memory):
    for rule_fact in first_rule_part:
        if rule_fact not in memory:
            return False

    return True

def conclusion_step(memory, rules, rule_is_active):
    is_change_active_rule = True

    while is_change_active_rule:
        is_change_active_rule = False
        for i in range(len(rules)):
            if rule_is_active[i][1] == [0] and is_active_rule(rules[i][0], memory):
                rule_is_active[i][1] = [1]
                memory += rules[i][1]
                is_change_active_rule = True

    return memory, rules, rule_is_active


def remove_row(table, row):
    tbl = table._tbl
    tr = row._tr
    tbl.remove(tr)

def move_last_row(t, row0):
    row1 = t.rows[-1]
    row0._tr.addnext(row1._tr)

if __name__ == '__main__':
    # memory = [1, 2, 3]
    # rules = [[[2, 5], [6]], [[1, 2], [4]]]
    # rule_is_active = [[[4], [0]], [[1, 2], [0]]]
    # description = [[[1, 2], ["block1", "ha ha"]]]
    # conclusion = [x[1] for x in description if is_active_rule(x[0], memory)]
    # memory, rules, rule_is_active = conclusion_step(memory, rules, rule_is_active)
    #
    # print(memory)
    # print(conclusion)

    doc = docx.Document('Пример ДИ.docx')
    # последовательность всех таблиц документа
    all_tables = doc.tables
    print('Всего таблиц в документе:', len(all_tables))

    # создаем пустой словарь под данные таблиц
    data_tables = {i: None for i in range(len(all_tables))}
    # проходимся по таблицам
    for i, table in enumerate(all_tables):
        print('\nДанные таблицы №', i)
        # создаем список строк для таблицы `i` (пока пустые)
        data_tables[i] = [[] for _ in range(len(table.rows))]
        # проходимся по строкам таблицы `i`
        for j, row in enumerate(table.rows):
            # проходимся по ячейкам таблицы `i` и строки `j`
            for cell in row.cells:
                # добавляем значение ячейки в соответствующий
                # список, созданного словаря под данные таблиц
                data_tables[i][j].append(cell.text)

        # смотрим извлеченные данные
        # (по строкам) для таблицы `i`
        print(data_tables[i])
        print('\n')

    # print('Данные всех таблиц документа:')
    # print(data_tables)

    cell_one_job_purpose = all_tables[1].rows[4]
    cell_main_responsibilities = all_tables[2].rows[0]
    cell_job_requirements = [[all_tables[2].rows[i].cells[0].text, all_tables[2].rows[i].cells[2]] for i in range(14, 20)]

    education = cell_job_requirements[0][1]
    experience = cell_job_requirements[1][1]
    state_secret = cell_job_requirements[2][1]
    knowledge = cell_job_requirements[3][1]
    languages = cell_job_requirements[4][1]
    software_knowledge = cell_job_requirements[5][1]

    print([_.text for _ in cell_one_job_purpose.cells])
    print([_.text for _ in cell_main_responsibilities.cells])
    print([_[0] for _ in cell_job_requirements])

    # 6 строк удалить из табдицы 2
    all_tables[2].rows[2].cells[0].merge(all_tables[2].rows[6].cells[2])
    remove_row(all_tables[2], all_tables[2].rows[2])

    new_row = all_tables[2].add_row()
    move_last_row(all_tables[2], all_tables[2].rows[1])
    # new_row = all_tables[2].add_row()
    # move_last_row(all_tables[2], all_tables[2].rows[1])
    # new_row = all_tables[2].add_row()
    # move_last_row(all_tables[2], all_tables[2].rows[1])


    cell_one_job_purpose.cells[0].text = "2"
    doc.save("Output.docx")
