countries = {
    'Algérie': {
        'answers': ['Alger', 'Tunis', 'Le Caire'],
        'good_answer_index': 0
    },
    'France': {
        'answers': ['Paris', 'Rome', 'Madrid'],
        'good_answer_index': 0
    },
    'Chine': {
        'answers': ['Shanghai', 'Pékin', 'Tokyo'],
        'good_answer_index': 2
    }
}

i = 0
good_answer = 0

for i, country in enumerate(countries):
    print(f"Quelle est la capitale du pays : {country} ?\n")
    for capital in countries[country]['answers']:
        print(f"{i + 1}: {capital} |", end=" ")
    print('')
    answer = input('').lower()
    answer_index = countries[country]['answers'].index(
        answer[0].upper() + answer[1:])
    if countries[country]['good_answer_index'] == answer_index:
        good_answer += 1
    print('')
print(f"Vous avez {good_answer} bonne(s) réponse(s) / 3")
