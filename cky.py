def cky(G, l):
  
  n = len(l)

  T = []

  for i in range(n+1):
    T.append([[] for _ in range(i)])

  for i in range(n):
    for key, values in G.items():
      for item in values:
        if l[i] == item:
          T[i+1][i].append(key)

  for m in range(2, n+1):
    for i in range((n-m) + 1):
      for j in range(i+1, i+m):
        for key, values in G.items():    
          for item in values:
            if len(item) == 2 and (item[0] in T[j][i]) and (item[1] in T[i+m][j]):
              T[i+m][i].append(key)
                
  if "S" in T[n][0]:
    return True
  else:
    return False
  


def main():
  c = int(input())
  for _ in range(c):
    l = input()
    n = [int(i) for i in l.split()]
    G = {}
    j = 0
    while j < n[0]:
      l = input()
      l = l.split()
      G[l[0]] = []
      for i in range(1,len(l)):
        G[l[0]].append(l[i])
      j+=1
    i = 0
    while i < n[1]:
      l = input()
      ans = cky(G,l)
      if ans:
        print('yes')
      else:
        print('no')
      i+=1
main()