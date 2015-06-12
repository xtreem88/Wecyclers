from time import clock
def check_repeated_number(number):
  repeated=False
  number=str(number)
  if len(number) == 2:
    if number[0] == number[1]:
      return True
  for i in range(0,len(number)-2):
    if number[i] == number[i+1]:
      repeated = True
    else:
      repeated = False
  return repeated

def recycle(a,b):
  total=0
  for t in range(a,b+1):
    for u in range(t+1,b+1):
      if str(t) in str(u)*2:
        res+=1
  return total

start = clock()
f=open('.input')
numbers=int(f.readline().rstrip('\r\n'))
i=1
out=open('.output','w')
while i<=numbers:
  read=f.readline().rstrip('\r\n')
  line=read.split()
  a=int(line[0])
  b=int(line[1])
  ans = recycle(a,b)
  

  print("Case #%s: %s"%(i,ans))
  out.write("Case #%s: %s \n"%(i,ans))
  i+=1
out.close()
f.close()
print ("Total time: "+`clock() - start`)
