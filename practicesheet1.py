Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20
>>> a+= 30;a%=3;print(a)
2
>>> true*false
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    true*false
NameError: name 'true' is not defined
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3)and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False is 'False'
False
>>> ((True == False) or  (False> True)) and (False <= True)
False
>>> ##3
>>> s1= 'Nice to have it'
>>> s2='here'
>>> s1 +' '+ s2
'Nice to have it here'
>>> #4
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> len(a)
6
>>> a[3][1][2]
['hello']
>>> a.insert(0,s1)
>>> a.insert(7,s2)
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> #6
>>> n=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
>>> for i in n :
	if i==237:
		print(i)
		break;
	elif x%2==0 :
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#36>", line 5, in <module>
    elif x%2==0 :
NameError: name 'x' is not defined
>>> for i in n :
	if i==237:
		print(i)
		break;
	elif i%2==0 :
		print(i)

		
386
462
418
344
236
566
978
328
162
758
918
237
>>> #7
>>> color_list_1 = set(['white','black', 'red'])
>>> color_list_2 = set(['red', 'green'])
>>> color_list_1
{'red', 'white', 'black'}
>>> color_list_1 - color_list_2
{'white', 'black'}
>>> #8
>>> #9
>>> b=int(input())
print(b + b*b + b*b*b )
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    b=int(input())
ValueError: invalid literal for int() with base 10: 'print(b + b*b + b*b*b )'
>>> b=int(input())
int(print(b + b*b + b*b*b ))
SyntaxError: multiple statements found while compiling a single statement
>>> or: multiple statements found while compiling a single statement
>>>b
SyntaxError: invalid syntax
>>> b=int(input())
print (int(b + b*b + b*b*b ))
SyntaxError: multiple statements found while compiling a single statement
>>> b=int(b.input())

print (int(b + b*b + b*b*b ))
SyntaxError: multiple statements found while compiling a single statement
>>> b=int(input())
print(b + b*b + b*b*b )
SyntaxError: multiple statements found while compiling a single statement
>>> b=int(input()):
print(b + b*b + b*b*b )
SyntaxError: invalid syntax
>>> d=int(input())
5
>>> print(d+ d*d+ d*d*d)
155
>>> 