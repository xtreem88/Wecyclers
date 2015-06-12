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
  c=[x for x in range(a,b+1)]
  for key,x in enumerate(c):
    if check_repeated_number(x) == False:
      for y in c[key+1:]:
          n=str(x)
          m=str(y)
          if len(n)==len(m) and len(n)>1 and len(m)>1:
             ki=1 
             while ki <len(n):
                 
                 temp=n[-1:-(ki)-1:-1][::-1]+n[:-(ki)]
                 if temp == n:
                   break
                 
                 if temp[0]!='0':
                  if temp==m:
                     total+=1
                     break
                 ki+=1   
          else :
              break
  return total

start = clock()
f=open('.input')
numbers=int(f.readline().rstrip('\r\n'))
i=1
out=open('.output2','w')
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
