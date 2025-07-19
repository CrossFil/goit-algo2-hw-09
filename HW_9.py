import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    # Початкова точка
    current = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current)

    for i in range(iterations):
        # Генерація сусідньої точки
        neighbor = current.copy()
        # Вибираємо випадкову координату для зміни
        idx = random.randint(0, len(bounds) - 1)
        # Додаємо невеликий крок
        step = random.uniform(-0.1, 0.1)
        neighbor[idx] += step

        # Перевірка меж
        neighbor[idx] = max(bounds[idx][0], min(bounds[idx][1], neighbor[idx]))

        neighbor_value = func(neighbor)

        # Якщо сусід кращий, переходимо до нього
        if neighbor_value < current_value:
            # Перевірка умови зупинки
            if abs(current_value - neighbor_value) < epsilon:
                break
            current = neighbor
            current_value = neighbor_value

    return current, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    # Найкраща знайдена точка
    best = [random.uniform(bound[0], bound[1]) for bound in bounds]
    best_value = func(best)

    for i in range(iterations):
        # Генерація випадкової точки
        candidate = [random.uniform(bound[0], bound[1]) for bound in bounds]
        candidate_value = func(candidate)

        # Якщо знайдена кращу точку
        if candidate_value < best_value:
            # Перевірка умови зупинки
            if abs(best_value - candidate_value) < epsilon:
                break
            best = candidate
            best_value = candidate_value

    return best, best_value


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    # Початкова точка
    current = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current)

    best = current.copy()
    best_value = current_value

    temperature = temp

    for i in range(iterations):
        # Перевірка умови зупинки за температурою
        if temperature < epsilon:
            break

        # Генерація сусідньої точки
        neighbor = current.copy()
        idx = random.randint(0, len(bounds) - 1)
        step = random.uniform(-0.5, 0.5)
        neighbor[idx] += step

        # Перевірка меж
        neighbor[idx] = max(bounds[idx][0], min(bounds[idx][1], neighbor[idx]))

        neighbor_value = func(neighbor)

        # Розрахунок ймовірності прийняття
        if neighbor_value < current_value:
            # Приймаємо кращий розв'язок
            current = neighbor
            current_value = neighbor_value

            # Оновлюємо найкращий розв'язок
            if neighbor_value < best_value:
                if abs(best_value - neighbor_value) < epsilon:
                    break
                best = neighbor.copy()
                best_value = neighbor_value
        else:
            # Приймаємо гірший розв'язок з певною ймовірністю
            delta = neighbor_value - current_value
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = neighbor
                current_value = neighbor_value

        # Охолодження
        temperature *= cooling_rate

    return best, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)

    # Hill Climbing:
    # Розв'язок: [0.0009950965436430481, 0.00019257948369554023] Значення: 1.0273039887107815e-06
    #
    # Random Local Search:
    # Розв'язок: [-0.035969273610665375, -0.04599787374073472] Значення: 0.0034095930327474808
    #
    # Simulated Annealing:
    # Розв'язок: [0.015226118053753512, 0.0009830364575736938] Значення: 0.00023280103166375767