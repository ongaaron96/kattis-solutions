name = input()
initials = list(map(lambda x: x[0], name.split('-')))
print(''.join(initials))
