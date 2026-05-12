def get_oldest(people):
    highest_age = max([person["age"] for person in people])
    return [person["name"] for person in people if person["age"] == highest_age]
