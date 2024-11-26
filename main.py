import random
num = [random.randint(-50, 50) for _ in range(25)]
num_positive = 0
num_negative = 0
num_nuli = 0
for number in num:
    if number > 0:
        num_positive += 1
    elif number < 0:
        num_negative += 1
    else:
        num_nuli += 1
total_num = len(num)
pol_percen =(num_positive / total_num) * 100
neg_percen =(num_negative / total_num) * 100
zero_percen = (num_nuli / total_num) * 100

max_num = max(num)
min_num = min(num)

print(f"список чисел {num}")
print("\nрезультат: ")
print(f"положительные числа: {num_positive} ({neg_percen} %)")
print(f"отрицательные числа: {num_negative } ({neg_percen} %)")
print(f"нули: {num_nuli} ({zero_percen} %)")
