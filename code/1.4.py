def pad(s, n):
    length = n - len(s)
    return s + " "*length

def padr(s, n):
    length = n - len(s)
    return " "*length + s

i1 = input("What is your first item?\n")
p1 = float(input("How much does '%s' cost?\n"%i1))
i2 = input("What is your second item?\n")
p2 = float(input("How much does '%s' cost?\n"%i2))
i3 = input("What is your third item?\n")
p3 = float(input("How much does '%s' cost?\n"%i3))

total = p1 + p2 + p3

print("┏━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃  Christopher's Shop   ┃")
print("┠───────────────────────┨")
print("┃                       ┃")
print("┃ %s £ %s ┃"%(pad(i1, 11), padr("%.2f"%p1, 7)))
print("┃ %s £ %s ┃"%(pad(i2, 11), padr("%.2f"%p2, 7)))
print("┃ %s £ %s ┃"%(pad(i3, 11), padr("%.2f"%p3, 7)))
print("┃                       ┃")
print("┠───────────────────────┨")
print("┃ %s %s ┃"%(pad("Total", 10), padr("£%.2f"%total, 10)))
print("┗━━━━━━━━━━━━━━━━━━━━━━━┛")
