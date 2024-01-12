N = len(s)
mother = 'aeiouAEIOU'
count = 0
for i in range(N):
  if i<N//2 and s[i] in mother: count += 1 
  if i>=N//2 and s[i] in mother: count -= 1 
if count==0: return True
else: return False              