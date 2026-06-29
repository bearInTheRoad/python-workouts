def generate_gematria():
    return {chr(i): i - 96 for i in range(97, 123)}


def gematria_for(word: str) -> int:
    return sum((generate_gematria().get(char, 0) for char in word))


print(generate_gematria())
print(gematria_for("cat"))
