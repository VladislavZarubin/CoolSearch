def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из 'latters', найденых в указанной фразе."""
    return set(letters).intersection(set(phrase))
