def group_anagrams(words):
    anagrams = {}
    for w in words:
        key = "".join(sorted(w))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(w)
    return list(anagrams.values())
