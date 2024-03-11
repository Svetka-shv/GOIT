# # Створення списків
# language = ['a', 'd', 'q']
# language.insert(3, 'f')
# print(language)
# print(type(language))
#
# # перетворення типів
# a = 'hello world'
# res = list(a)
# print(res)
#
# # split
# res = 'd/f/g/h/jj/k/kl/l'
# res = res.split('/')
# print(res)


# index
# language = ['a', 'd', 'q', 'xx', 'yyy']
# print(language[3])
# print(language[-1])
# print(language.index('xx'))


language_1 = ['a', 'd', 'q', 'xx', 'yyy']
language_2 = ['a', 'erer', 'sfdfd']
lan_3 = [language_1, language_2]
print(lan_3[1][1])
language_1.append('dsadfdsd')
print(language_1)