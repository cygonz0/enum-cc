
import sys

def luhn(n):

    sum = 0

    alt = 0

    i = len(n) - 1

    num = 0
    
    while i >= 0:

       num = int(n[i])

       if alt:

          num = num * 2

          if num > 9:

             num = ( num % 10 ) + 1  

       sum = sum + num 
 
       alt = not alt 

       i -= 1
   
    return sum%10 == 0

if __name__ == "__main__":

     if len(sys.argv) != 2:

        print "Usage: python enum-cc.py <CC first 12-digit here>"

        sys.exit()

     digits = sys.argv[1]
     for i in xrange(9999):
      x = '{0:04}'.format(i)

      n = digits + x
      if luhn(n):

         print "Valid CC Number Found: " + digits + x

