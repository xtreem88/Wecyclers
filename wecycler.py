f=open('.input')
numbers=int(f.readline().rstrip('\r\n'))
i=1
out=open('.output','w')
while i<=numbers:
  read=f.readline().rstrip('\r\n')
  line=read.split()
  a=int(line[0])
  b=int(line[1])
  total=0
  c=[x for x in range(a,b+1)]
  for key,x in enumerate(c):
      for y in c[key+1:]:
          n=str(x)
          m=str(y)
          if len(n)==len(m) and len(n)>1 and len(m)>1:
             ki=1 
             while ki <len(n):
                 temp=n[-1:-(ki)-1:-1][::-1]+n[:-(ki)]
                 if temp[0]!='0':
                  if temp==m:
                     total+=1
                     break
                 ki+=1   
          else :
              break


  print("Case #%s: %s"%(i,total))
  out.write("Case #%s: %s \n"%(i,total))
  i+=1
out.close()
f.close()
