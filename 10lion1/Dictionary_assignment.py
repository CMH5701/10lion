Dic = {}
while True:
    key = int(input())
    value = (input())
    if key == '0' or value =='문자열 종료':
        print("그만")
        print(Dic)
        break
    else:
        Dic[key] = value

print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items()))
