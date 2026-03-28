from Vector import (
    read_vectors,
    max_dimension_vector,
    max_length_vector,
    average_length,
    count_above_average,
    max_component_vector,
    min_component_vector
)

def main():
    vectors = read_vectors("input01.txt")
    # vectors = read_vectors("input02.txt")
    # vectors = read_vectors("input03.txt")
    # vectors = read_vectors("input04.txt")

    v1 = max_dimension_vector(vectors)
    print("\nНайбільша розмірність:", v1)

    v2 = max_length_vector(vectors)
    print("Найбільша довжина:", v2)

    avg_len = average_length(vectors)
    print("Середня довжина:", round(avg_len, 2))

    count = count_above_average(vectors)
    print("Кількість > середньої:", count)

    v3 = max_component_vector(vectors)
    print("Макс компонента у вектора:", v3)

    v4 = min_component_vector(vectors)
    print("Мін компонента у вектора:", v4)

if __name__ == "__main__":
    main()
