import timeit
from pathlib import Path


def compute_lps(pattern: str) -> list[int]:
    """Compute the longest prefix suffix (LPS) array for the given pattern.

    :param pattern: The pattern for which to compute the LPS array.
    :return: LPS array.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> list[int]:
    """Perform Knuth-Morris-Pratt (KMP) search to find all occurrences of the pattern in the text.

    :param text: The text in which to search for the pattern.
    :param pattern: The pattern to search for.
    :return: A list of starting indices where the pattern is found in the text.
    """
    pattern_len = len(pattern)
    text_len = len(text)

    lps = compute_lps(pattern)

    i = j = 0
    found_indices = []

    while i < text_len:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_len:
            found_indices.append(i - j)
            j = lps[j - 1]

        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return found_indices


def build_shift_table(pattern: str) -> dict[str, int]:
    """Build the shift table for the Boyer-Moore algorithm.

    :param pattern: The pattern for which to build the shift table.
    :return: The shift table.
    """
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text: str, pattern: str) -> list[int]:
    """Perform Boyer-Moore search to find all occurrences of the pattern in the text.

    :param text: The text in which to search for the pattern.
    :param pattern: The pattern to search for.
    :return: A list of starting indices where the pattern is found in the text.
    """
    shift_table = build_shift_table(pattern)
    i = 0
    found_indices = []
    pattern_len = len(pattern)
    text_len = len(text)

    while i <= text_len - pattern_len:
        j = pattern_len - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            found_indices.append(i)
            i += (
                shift_table.get(text[i + pattern_len - 1], pattern_len)
                if i + pattern_len < text_len
                else 1
            )
        else:
            i += shift_table.get(text[i + pattern_len - 1], pattern_len)

    return found_indices


def rabin_karp_search(text: str, pattern: str) -> list[int]:
    """
    Perform Rabin-Karp search to find all occurrences of the pattern in the text.

    Parameters:
    text (str): The text in which to search for the pattern.
    pattern (str): The pattern to search for.

    Returns:
    List[int]: A list of starting indices where the pattern is found in the text.
    """
    alphabet_size = 256
    prime_number = 101
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    hash_multiplier = 1
    found_indices = []

    for i in range(pattern_length - 1):
        hash_multiplier = (hash_multiplier * alphabet_size) % prime_number

    for i in range(pattern_length):
        pattern_hash = (alphabet_size * pattern_hash + ord(pattern[i])) % prime_number
        text_hash = (alphabet_size * text_hash + ord(text[i])) % prime_number

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if text[i : i + pattern_length] == pattern:
                found_indices.append(i)
        if i < text_length - pattern_length:
            text_hash = (
                alphabet_size * (text_hash - ord(text[i]) * hash_multiplier)
                + ord(text[i + pattern_length])
            ) % prime_number
            if text_hash < 0:
                text_hash = text_hash + prime_number

    return found_indices


def load_text(file_path: Path) -> str:
    """
    Load text from a file.

    Parameters:
    file_path (Path): The path to the file.

    Returns:
    str: The content of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def measure_time(search_func, text: str, pattern: str) -> float:
    """
    Measure the execution time of a search function.

    Parameters:
    search_func (callable): The search function to measure.
    text (str): The text in which to search for the pattern.
    pattern (str): The pattern to search for.

    Returns:
    float: The execution time in seconds.
    """
    start_time = timeit.default_timer()
    search_func(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


if __name__ == "__main__":
    # Load texts
    text1 = load_text(Path("text1.txt"))
    text2 = load_text(Path("text2.txt"))

    # Patterns for testing
    existing_pattern = "Висновки"
    non_existing_pattern = "ловіармрівоармівм"

    # Measure time
    results = {
        "KMP": {"text1": {}, "text2": {}},
        "Boyer-Moore": {"text1": {}, "text2": {}},
        "Rabin-Karp": {"text1": {}, "text2": {}},
    }

    # Measure time for existing pattern
    results["KMP"]["text1"]["existing"] = measure_time(
        kmp_search, text1, existing_pattern
    )
    results["KMP"]["text2"]["existing"] = measure_time(
        kmp_search, text2, existing_pattern
    )
    results["Boyer-Moore"]["text1"]["existing"] = measure_time(
        boyer_moore_search, text1, existing_pattern
    )
    results["Boyer-Moore"]["text2"]["existing"] = measure_time(
        boyer_moore_search, text2, existing_pattern
    )
    results["Rabin-Karp"]["text1"]["existing"] = measure_time(
        rabin_karp_search, text1, existing_pattern
    )
    results["Rabin-Karp"]["text2"]["existing"] = measure_time(
        rabin_karp_search, text2, existing_pattern
    )

    # Measure time for non-existing pattern
    results["KMP"]["text1"]["non_existing"] = measure_time(
        kmp_search, text1, non_existing_pattern
    )
    results["KMP"]["text2"]["non_existing"] = measure_time(
        kmp_search, text2, non_existing_pattern
    )
    results["Boyer-Moore"]["text1"]["non_existing"] = measure_time(
        boyer_moore_search, text1, non_existing_pattern
    )
    results["Boyer-Moore"]["text2"]["non_existing"] = measure_time(
        boyer_moore_search, text2, non_existing_pattern
    )
    results["Rabin-Karp"]["text1"]["non_existing"] = measure_time(
        rabin_karp_search, text1, non_existing_pattern
    )
    results["Rabin-Karp"]["text2"]["non_existing"] = measure_time(
        rabin_karp_search, text2, non_existing_pattern
    )

    # Print results
    for algo, texts in results.items():
        print(f"\n{algo} algorithm:")
        for text_name, patterns in texts.items():
            for pattern_type, time in patterns.items():
                print(f"  {text_name} - {pattern_type} pattern: {time:.6f} seconds")
