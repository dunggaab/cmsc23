def doubledInt(x:int) -> int:
      return (x*2)

def largest(x:float,y:float) -> float:
      if x>y:
          return (x)
      else:
          return (y)

def isVertical(a:(float,float),b:(float,float)) -> bool:
      if a [0] == b [0]:
            return True
      else:
            return False

def primes(n:int) -> [int]:
      prime = []
      num=2
      flag=False
      if num==2:
          prime.append (num)
      while (len(prime)<n):
            for i in range (2,num):
                  if num % i == 0:
                        flag=False
                        break
                  else:
                        flag=True
            if flag==True:
                  prime.append (num)
            num += 1
      return prime
      

def fibonacciSequence(n:int) -> [int]:
      c= 0
      a= 0
      b= 1
      i = 0
      fib = []
      while (i<n):
                  fib.append (a)
                  c= a + b
                  a = b
                  b = c
                  i += 1

      return fib

def sortedIntegers(l:[int]) -> [int]:
  for i in range (len (l)):
    flag=False
    for j in range (0, len (l)-i-1):
      if l[j]> l[j+1]:
        temp = l [j]
        l [j] = l [j+1]
        l [j+1] = temp

        flag= True
        
    if not flag:
      break

  return l

def sublists(l:[int]) -> [[int]]:
  sublist = [[]]
  for i in range (len(l)+1):
    for j in range (i):
      sublist.append (l[j: i])
  return sublist
