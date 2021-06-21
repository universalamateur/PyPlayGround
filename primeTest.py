#!/usr/bin/python

def primeOrNot(number):
    if number==1 or (number % 2 == 0 and number > 2):
        return "Not prime"
    for i in range(3, int(number**(1/2))+1, 2):
    #if divisible
        if number % i == 0:
            return "Not prime"
    return "Prime"
 
if __name__ == "__main__":
  dataSet=[1000000007,100000003,1000003]
  for data in dataSet:
      print(primeOrNot(data))