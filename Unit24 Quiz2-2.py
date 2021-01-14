a = list(map(int, input().split(';')))
a.sort(reverse = True)
for i in a:
    print('{0:>9,}'.format(i))