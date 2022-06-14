from tree_utils import DELIMITER


def horspool(text: str, pattern: str):
    comparisons = 0
    print("Performing Horspool's algorithm with text: {} and pattern: {}".format(text, pattern))
    bad_match = {}
    for index, i in enumerate(pattern):
        if index == len(pattern) - 1:
            if i not in bad_match:
                bad_match[i] = len(pattern)
        else:
            bad_match[i] = len(pattern) - index - 1

    print("Bad match dictionary/table for pattern {}: {}".format(pattern, bad_match))

    pattern_index = 0
    pattern_cmp = len(pattern) - 1
    text_cmp = pattern_index + len(pattern) - 1

    while pattern_index < len(text) + 1 - len(pattern):
        print(DELIMITER)
        first_char = text[text_cmp]
        print(f"Pattern is currently located at {pattern_index}. The first char being compared is {first_char}. Pattern looks like this: ")
        print(' '.join([i for i in text]))
        print(' ' * pattern_index * 2 + ' '.join([i for i in pattern]))

        while pattern_cmp > -1 and pattern[pattern_cmp] == text[text_cmp]:
            comparisons += 1
            print("equal comparison")
            pattern_cmp -= 1
            text_cmp -= 1

        if pattern_cmp == -1:
            print("Found at index:", pattern_index, " Number of comparisons:", comparisons)
            return pattern_index
        else:
            comparisons += 1
            print(f"Mismatch found at index {text_cmp} in text. Character mismatched is text: {text[text_cmp]} pattern: {pattern[pattern_cmp]}")
            pattern_cmp = len(pattern) - 1
            if first_char not in bad_match:
                print(f"Shifting pattern by {len(pattern)} because first char being compared {first_char} is not in bad match table")
                pattern_index += len(pattern)
            else:
                print(f"Shifting pattern by {bad_match[first_char]} because first char being compared {first_char} has a bad match value of {bad_match[first_char]}")
                pattern_index += bad_match[first_char]

            text_cmp = pattern_index + len(pattern) - 1
            print(f"New pattern index is {pattern_index}. Comparisons so far: {comparisons}")

    print("Not found. Number of comparisons:", comparisons)
