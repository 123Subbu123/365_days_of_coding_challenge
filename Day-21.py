## 28.Get index in the list of objects by attributes in Python.
class X:
  def __init__(self,val):
    self.val=val

def getIndex(li,target):
  for index, X in enumerate(li):
    if X.val==target:
      return index
  return -1

li = [1,2,3,4,5,6]
a=list()
for i in li:
  a.append(X(i))
print(getIndex(a,3))