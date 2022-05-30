List = []
a=15;

for i in range(a) :
    number = int(input())
    List.append(number)
if (a==15):
    print(List)
for a in List:
    if a % 2 ==0:
        List.remove(a)
print(List)
for b in List:
    if b % 3 ==0:
        List.remove(b)
print(List)
print(List.pop(0))
List.insert(0,2)
List.insert(1,3)
List.sort()
print(List)
