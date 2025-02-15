users = {"Tom", "Bob", "Alice"}

users.discard("Tim")  # элемент "Tim" отсутствует, и метод ничего не делает
print(users)  # {"Tom", "Bob", "Alice"}

users.discard("Tom")  # элемент "Tom" есть, и метод удаляет элемент
print(users)  # {"Bob", "Alice"}