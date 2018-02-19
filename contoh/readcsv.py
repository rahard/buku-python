f = open('data.txt', 'r')

x = []
y = []
while True:
   line = f. readline()
   if not line: 
       break
   line = line.rstrip()
   a,b = line.split(',')
   x.append(int(a))
   y.append(int(b))

print x,y
