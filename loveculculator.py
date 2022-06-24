print('Welcome to the love calculator!')
name1=input('Enter  your name : ')
name2=input('Enter the name of your crush :' )
combined_names=name1 + name2
names_lower_case=combined_names.lower()
t= names_lower_case.count('t')
r= names_lower_case.count('r')
u= names_lower_case.count('u')
e= names_lower_case.count('e')

true= t+r+u+e

l= names_lower_case.count('l')
o= names_lower_case.count('o')
v= names_lower_case.count('v')
e= names_lower_case.count('e')

love= l+o+v+e
love_score= str(true) + str(love)
score=int(love_score)
print(f'Your love score is {love_score} % .')

if score>=55 and score<=100:
  print('congratulations!Theres is true love between you')
elif score>=40 and score<55:
  print('You love score is below target score')
else:
  print('There is no love at all')