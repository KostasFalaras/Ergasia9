x = input ('Give an int')
x = int(x)
fora=1

while x>9 or fora==1:
    x = 3*x
    x = x + 1
    sum = 0
    while x>0 :
       sum = sum + x%10
       x = x/10
       x = int(x)
    x = sum
    fora = 2
print (sum)
  








