def count_words(sentence: str) -> int:
    if not sentence or not sentence.strip():
        return 0
    return len(sentence.split())


def find_unique(items: list) -> list:
    unique = []
    for x in items:
        if x not in unique:
            unique.append(x)
    # Теперь оставляем только те, что встречаются один раз
    result = []
    for x in unique:
        count = 0
        for y in items:
            if x == y:
                count += 1
        if count == 1:
            result.append(x)
    return result


def is_palindrome(value) -> bool:
    s = str(value).lower()
    return s == s[::-1]


def are_anagrams(str1: str, str2: str) -> bool:
    w1 = str1.lower()
    w2 = str2.lower()

    if len(w1) != len(w2):
        return False

    # Преобразуем в списки букв
    letters1 = []
    for ch in w1:
        letters1.append(ch)

    letters2 = []
    for ch in w2:
        letters2.append(ch)

    # Пытаемся "съесть" все буквы из letters1 из letters2
    i = 0
    while i < len(letters1):
        ch = letters1[i]
        found = False
        j = 0
        while j < len(letters2):
            if letters2[j] == ch:
                del letters2[j]
                found = True
                break
            j += 1
        if not found:
            return False
        i += 1

    return len(letters2) == 0


def combine_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()
    result.update(dict2)
    return result