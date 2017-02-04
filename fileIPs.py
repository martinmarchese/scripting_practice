# set para no repetir valores
ips = set()

# leo linea por linea y los agrego al set
for line in open('ips','r'):
    ips.add(line)

# uso sorted de python, mezcla entre merge y insertion sort (TimSort)
print sorted(ips,reverse=True)
