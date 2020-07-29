
def power(n, m):
  if m == 0:
    return 1
  elif m == 1:
    return n
  else:
    return n*power(n, m-1)

counter = 0
success = True
n = 0
m = 0

for i in range(0,100):
  for j in range(0,100):
    counter = counter + 1
    if i**j != power(i,j):
      success = False
      n = str(i)
      m = str(j)
      break

if success:
  print("All true.", end=" ")
else:
  print("Failure at ("+n+"**"+m+").", end=" ")

print("Counted", counter, "operations.")
