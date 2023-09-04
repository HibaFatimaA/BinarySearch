
class BSTNode:
  '''
  Fields:
     val (Int)
     lchild (anyof BSTNode None)
     rchild (anyof BSTNode None)
     
  Requires:
     Every val of each node in lchild is less than val
     Every val of each node in rchild is greater than val
  '''
  
  def __init__(self, value, left, right):
    '''
    initializes self so that val is value, lchild is left, and rchild
    is right
    
    Effects: mutates self
    
    __init__: BSTNode (Int) (anyof BSTNode None) (anyof BSTNode None) => None
    ''' 
    self.val = value
    self.lchild = left
    self.rchild = right
  
  def __eq__(self, other):
    '''
    Returns True if self and other are equal, and False otherwise.
    
    __repr__: BSTNode Any => Bool
    ''' 
    return isinstance(other, BSTNode) and \
    self.val == other.val and \
    self.lchild == other.lchild and \
    self.rchild == other.rchild
  
  def __repr__(self):
    '''
    Returns a string representation of self where the values are in numeric 
    order each separated by a comma.
    
    __repr__: BSTNode => Str
    ''' 
    node = self
    ans = '{0.val}'
    if node.val == None:
      return '' 
    if node.lchild != None:
      ans += ', '+ repr(node.lchild)
    if node.rchild != None:
      ans += ', '+ repr(node.rchild)
    r = ans.format(node)
    w = r.split(', ')
    w.sort(key = int)
    rep = (', '.join(w))
    return rep
    
def contains(root, item):
  '''
    Returns True if item is in root which is a BST and False if it is not 
    in root. 
    
    contains: BSTNode Any => Bool
    
    Examples:
      M = BSTNode(None, None, None)
      contains(M, 388), 0) => False
      
      M = BSTNode(None, None, None)
      contains(M, 388), 'cat') => False
    ''' 
  if root.val == None:
    return False
  if root.val == item:
    return True
  if type(item) != int:
    return False
  elif (root.val > item) and (root.lchild != None):
    return contains(root.lchild, item)
  elif (root.val < item) and (root.rchild != None):
    return contains(root.rchild, item)
  else:
    print('what')
    return False

##Examples:
M = BSTNode(None, None, None)
##check.expect("example 1 Test", contains(M, 0), False)
##check.expect("example 2 testing", contains(M, 'cat'), False)

##Tests:
B = BSTNode(123, BSTNode(3, None, None), None)
##check.expect("MarkUs Basic Test __init__", B.val == 123, True)
##check.expect("MarkUs Basic Test __init__", B.lchild.val == 3, True)
##check.expect("MarkUs Basic Test __init__", B.rchild == None, True)
##check.expect("MarkUs Basic Test __init__", B.lchild.lchild == None, True)
##check.expect("MarkUs Basic Test __init__", B.lchild.rchild == None, True)

##testing init
M = BSTNode(522191, None, None)
##check.expect("init test 1", M.val, 522191)
##check.expect("test 2", M.lchild, None)
##check.expect("test 2", M.rchild, None)

##Testing Eq
B1 = BSTNode(388, None, None)
##B2 = BSTNode(388, None, None)
##check.expect("MarkUs Basic Test __eq__", B1==B2, True)

B1 = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, 51))
B2 = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, 51))
#check.expect("Test eq multiple values", B1==B2, True)

B1 = BSTNode(37, BSTNode(9, None, None), BSTNode(97, None, 51))
B2 = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, 51))
#check.expect("Test eq false values", B1==B2, False)

##Testing repr
B2 = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, 51))
#check.set_print_exact("9, 37, 47, 51")
#check.expect("Test __repr__ multiple values", print(B2), None)

B1 = BSTNode(2, None, None)
#check.set_print_exact("2")
#check.expect("single val __repr__", print(B1), None)

B3 = BSTNode(None, None, None)
#check.set_print_exact("")
#check.expect("None val __repr__", print(B3), None)

##test contains
M = BSTNode(388, None, None)
#check.expect("a contains Test", contains(M, 388), True)

M = BSTNode(388, None, None)
#check.expect("contains Test False", contains(M, 38), False)

B = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, None))
#check.expect("test 1 testing", contains(B, 47), True)
#check.expect("contains testing", contains(B, True), False)
#check.expect("contains testing", contains(B, 'cat'), False)

