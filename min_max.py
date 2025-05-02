def find_min_max(arr):
    # Базовий випадок для одного елемента
    if len(arr) == 1:
        return arr[0], arr[0]
    
    # Якщо масив має більше одного елемента, ділимо його на дві частини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    # Повертаємо мінімум та максимум з обох частин
    return min(left_min, right_min), max(left_max, right_max)

# Приклад використання:
arr = [3, 1, 5, 7, 2, 4, 6]
result = find_min_max(arr)
print(result)  # Виведе (1, 7)
