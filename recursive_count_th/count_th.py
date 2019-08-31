"""
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    index = len(word) - 2

    def counter(n, total=0):

        if word[n : n + 2] == "th":
            total += 1

        if n <= 0:
            return total
        else:
            return counter(n - 1, total)

    answer = counter(index, 0)
    return answer


print(count_th("thougth"))

