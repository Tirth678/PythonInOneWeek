# Check that a tuple type cannot be changed in python.
# tuple is represent by (1,2,3)
a = (1,2,3)
a.insert(0, 12)
# error as only indexing and couting is available