# 1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта
# формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.

# Вариант 5. Предприятие может предоставить работу по одной специальности 2 женщинам, по другой - 2 мужчинам,
# по третьей - 2 работникам независимо от пола. Сформировать все возможные варианты заполнения вакантных мест,
# если имеются 6 претендентов: 3 женщины и 3 мужчины.

from timeit import default_timer # импорта наиболее точного таймера из модуля timeit
from itertools import combinations
# Претенденты
women = ['Ж1', 'Ж2', 'Ж3'] # список женщин
men = ['М1', 'М2', 'М3'] # список мужчин

# Вариант 1: Алгоритмический способ
print("\nВариант 1: Алгоритмический")
start_time = default_timer()
all_combinations_manual = []
# Перебираем все пары женщин
for women_pair in combinations(women, 2):
    # remaining_women — одна оставшаяся женщина, которая не вошла в пару
    remaining_women = [w for w in women if w not in women_pair]
    # Перебираем все пары мужчин
    for men_pair in combinations(men, 2):
        # remaining_men — один оставшийся мужчина, который не вошел в пару
        remaining_men = [m for m in men if m not in men_pair]
        # Оставшиеся кандидаты (по одному от каждого пола) - на специальность 3.
        remaining = remaining_women + remaining_men
        # Сохраняем вариант
        all_combinations_manual.append({
            'специальность 1': list(women_pair),
            'специальность 2': list(men_pair),
            'специальность 3': remaining
        })
end_time = default_timer()
print(f"Всего комбинаций (алгоритмический): {len(all_combinations_manual)}")
for idx, combo in enumerate(all_combinations_manual, 1):
    print(f"{idx}. {combo}")
print(f"Время выполнения (алгоритмический): {(end_time - start_time)*10} секунд\n")

# Вариант 2: С помощью функций Питона
print("\nВариант 2: Через itertools")
start_time = default_timer()
all_combinations_itertools = []
# Цикл по женщинам: выбирается пара женщин
for w_comb in combinations(women, 2):
    # rem_w — одна оставшаяся женщина
    rem_w = [w for w in women if w not in w_comb]
    # Цикл по мужчинам: выбирается пара мужчин
    for m_comb in combinations(men, 2):
        # rem_m — один оставшийся мужчина
        rem_m = [m for m in men if m not in m_comb]
        # Оставшиеся кандидаты объединяются в одну группу
        rem = rem_w + rem_m
        # Сохранение комбинации
        all_combinations_itertools.append({
            'специальность 1': list(w_comb),
            'специальность 2': list(m_comb),
            'специальность 3': rem
        })
end_time = default_timer()
print(f"Всего комбинаций (itertools): {len(all_combinations_itertools)}")
for idx, combo in enumerate(all_combinations_itertools, 1):
    print(f"{idx}. {combo}")
print(f"Время выполнения (itertools): {(end_time - start_time)*10} секунд")