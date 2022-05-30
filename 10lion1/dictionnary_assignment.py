Dic1 = {'name' : '최명환' ,'age' : '24','birth' :991218 , 'sex' : 'man' ,"number" : '010-6259-8837'}
Dic2 = {'name' : '최재훈' ,'age' : '24','birth' :990101 , 'sex' : 'man' , 'number' : '010-4737-0960'}
Dic3 = {'name' : '천우희' ,'age' : '35','birth' :870420 , 'sex' : 'woman' , 'number' : '010-1004-1004'}
name= [1,2,3]
name[0:2]= [Dic1['name'] ,Dic2['name'],Dic3['name']]
age= [1,2,3]
age[0:2]= [Dic1['age'] ,Dic2['age'],Dic3['age']]
birth= [1,2,3]
birth[0:2]= [Dic1['birth'] ,Dic2['birth'],Dic3['birth']]
sex= [1,2,3]
sex[0:2]= [Dic1['sex'] ,Dic2['sex'],Dic3['sex']]
number= [1,2,3]
number[0:2]= [Dic1['number'] ,Dic2['number'],Dic3['number']]
print("이름 리스트는" ,name[0],name[1],name[2])
print("나이 리스트는" ,age[0],age[1],age[2])
print("생일 리스트는" ,birth[0],birth[1],birth[2])
print("성별 리스트는" ,sex[0],sex[1],sex[2])
print("전화번호 리스트는" ,number[0],number[1],number[2])
