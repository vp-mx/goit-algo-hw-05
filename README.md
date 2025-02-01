# Comparison of Substring Search Algorithm Efficiency

This project compares the efficiency of three substring search algorithms:
 - Knuth-Morris-Pratt,
 - Boyer-Moore,
 - and Rabin-Karp.

We measured the execution time of each algorithm on two text files (text1.txt and text2.txt) for two types of substrings: one that actually exists in the text and another that is fictional.

## Execution Time (in seconds)

| Algorithm    | Text   | Existing Substring | Fictional Substring |
|--------------|--------|--------------------|---------------------|
| KMP          | text 1 | 0.003291           | 0.003211            |
| KMP          | text 2 | 0.004782           | 0.004889            |
| Boyer-Moore  | text 1 | 0.000647           | 0.000324            |
| Boyer-Moore  | text 2 | 0.000966           | 0.000471            |
| Rabin-Karp   | text 1 | 0.004345           | 0.004857            |
| Rabin-Karp   | text 2 | 0.006318           | 0.007809            |

## Conclusions

The Boyer-Moore algorithm showed the best efficiency for both texts, especially for cases with an existing substring. The KMP algorithm also demonstrated good performance and stability. The Rabin-Karp algorithm, although it has its advantages, generally lags behind the other two algorithms in terms of execution speed.