a = map(str, input(). split())
count = 0
for words in a:
    if(words.strip(',.') == 'the'):
        count +=1
print(count)
