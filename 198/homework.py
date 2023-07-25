from hashmap import HashMap


def main():
    hashmap1 = HashMap(4)
    ret = hashmap1.put("1", "Алексей")
    ret = hashmap1.put("2", "Борис")
    ret = hashmap1.put("3", "Василий")
    ret = hashmap1.put("4", "Григорий")
    ret = hashmap1.put("5", "Дмитрий")
    ret = hashmap1.put("6", "Елена")
    ret = hashmap1.put("7", "Ёлка")
    ret = hashmap1.put("8", "Женя")
    ret = hashmap1.put("9", "Зинанда")
    ret = hashmap1.put("10", "Иван")

    print(f"hashmap1 содержит элементов: {len(hashmap1)} ")
    for bucket in hashmap1:
        print(f'Bucket {bucket.index}, bucket size - {len(bucket)}', end=":\n")
        for node in bucket:
            print(node)


if __name__ == "__main__":
    main()
