from time import clock
def recycle(a,b):
  total=0
  #start count at n = a and all the way to b (a<=n<m<=b)
  for n in range(a,b+1):
    #start m at n+1 all the way to b (n<m<=b)
    for m in range(n+1,b+1):
      #if n is in m*2 eg(1234 in 3451234512) then its recycled
      if str(n) in str(m)*2:
        #add the count
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
  ans = recycle(a,b)
  #print the outpot and store in the output file
  print("Case #%s: %s"%(i,ans))
  out.write("Case #%s: %s \n"%(i,ans))
  i+=1
#close the file handles
out.close()
f.close()
#Stop the clock and show the time
print ("Total time: "+`clock() - start`)
