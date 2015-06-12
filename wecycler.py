from time import clock
def wecycle(a,b):
  total=0
  multiplier = 1
  temp = a
  #get the multiplier for the a 
  while (temp >= 10):
    multiplier *= 10
    temp /= 10  
  #loop from a to b
  for n in range(a,b+1):
    #store n in m
    m=n
    while (True):
      #shift the values by moving decimal points
      m = (m / 10) + ((m % 10) * multiplier)
      #if they are equal, then break
      if (m == n):
        break
      #check the conditions
      if (m > n and m <= b):
        total+=1
  return total
#start the clock
start = clock()
#open the input file
f=open('.input')
#get the first line that contains the number of test cases
numbers=int(f.readline().rstrip('\r\n'))

#open output file
out=open('.output','w')
#loop through all the cases
i=1
while i<=numbers:
  #read each test case and put the values in a,b
  read=f.readline().rstrip('\r\n')
  line=read.split()
  a=int(line[0])
  b=int(line[1])
  #run the check recycle function
  ans = wecycle(a,b)
  #print the output and store in the output file
  print("Case #%s: %s"%(i,ans))
  out.write("Case #%s: %s \n"%(i,ans))
  i+=1
#close the file handles
out.close()
f.close()
#Stop the clock and show the time
print ("Total time: "+`clock() - start`)
