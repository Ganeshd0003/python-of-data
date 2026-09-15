import copy

# Normal operation

a = [1, 2, 3, 4, 5, 6, 7, 8]

print(a)

a.append(9)

print(a)

print()


# Copy 1D
# copy() creates a new list.
# Since this is a simple 1D list, changes to c do not affect b.

b = [1, 2, 3]

print(b)

c = b.copy()

print(c)

c.append(10)

print(f"b -> {b} | c -> {c}")

print()


# Copy 2D
# copy() creates a new OUTER list,
# but the INNER lists are still shared.
# Therefore, changing an inner list through bb
# also affects aa.
#
# This is called a SHALLOW COPY.
#
# To completely separate nested objects,
# use deepcopy().

aa = [[9, 7], [8, 6]]

print(aa)

bb = aa.copy()

print(bb)

bb[0].append(100)

print(f"aa -> {aa} | bb -> {bb}")


# Deep copy
# deepcopy() creates a completely independent copy,
# including the inner lists.

dd = copy.deepcopy(aa)

# Normal operation
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
a.append(9)
print(a)

print()

# Copy 1D
b = [1, 2, 3]
print(b)
c = b.copy()
print(c)
c.append(10)
print(f"b-> {b} | c-> {c}")

print()

# Copy 2D (we make copy but it's outer list copy only
# and inner list is shallow copy means we do changes in one it reflects in another becuase they linked    SO to overcome that we use deepcopy())
aa = [[9, 7], [8, 6]]
print(aa)
bb = aa.copy()
print(bb)
bb[0].append(100)
print(f"aa-> {aa} | bb-> {bb}")

print()

# 2D deepcopy
aaa = [[1, 2, 3], [4, 5, 6]]
print(aaa)
bbb = copy.deepcopy(aaa)
print(bbb)
bbb[0].append(1000)
print(f"aaa-> {aaa} | bbb-> {bbb}")

dd[0].append(200)

print(f"aa -> {aa} | dd -> {dd}")
