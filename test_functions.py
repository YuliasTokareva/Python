from functions import count_words, find_unique, is_palindrome, are_anagrams, combine_dicts


# Задача 1
def test_count_words_normal():
    assert count_words("Hello world") == 2

def test_count_words_single():
    assert count_words("Python") == 1

def test_count_words_empty():
    assert count_words("") == 0

def test_count_words_only_spaces():
    assert count_words("   ") == 0

def test_count_words_extra_spaces():
    assert count_words("  a  b  c  ") == 3


#  Задача 2
def test_find_unique_normal():
    assert find_unique([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]

def test_find_unique_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_find_unique_no_unique():
    assert find_unique([1, 1, 2, 2]) == []

def test_find_unique_empty():
    assert find_unique([]) == []

def test_find_unique_with_strings():
    assert find_unique(["a", "b", "a", "c"]) == ["b", "c"]


# Задача 3
def test_is_palindrome_word():
    assert is_palindrome("топот") == True

def test_is_palindrome_number():
    assert is_palindrome(12321) == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") == False

def test_is_palindrome_case():
    assert is_palindrome("Анна") == True

def test_is_palindrome_single_char():
    assert is_palindrome("a") == True

def test_is_palindrome_empty():
    assert is_palindrome("") == True


# Задача 4
def test_are_anagrams_yes():
    assert are_anagrams("listen", "silent") == True

def test_are_anagrams_no():
    assert are_anagrams("hello", "world") == False

def test_are_anagrams_case_and_spaces():
    assert are_anagrams("The Eyes", "They See") == True

def test_are_anagrams_different_lengths():
    assert are_anagrams("abc", "ab") == False

def test_are_anagrams_empty():
    assert are_anagrams("", "") == True


# Задача 5
def test_combine_dicts_normal():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 3, "c": 4}

def test_combine_dicts_empty_first():
    assert combine_dicts({}, {"x": 1}) == {"x": 1}

def test_combine_dicts_empty_second():
    assert combine_dicts({"x": 1}, {}) == {"x": 1}

def test_combine_dicts_both_empty():
    assert combine_dicts({}, {}) == {}

def test_combine_dicts_no_overlap():
    d1 = {"a": 1}
    d2 = {"b": 2}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 2}