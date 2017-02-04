#uso dict para no tener TODAS las URLs del archivo en memoria
urls = dict()

#por cada linea de archivo lo agrego al dict
for line in open('urls','r'):
    urls[line] = urls.get(line,0) + 1

# uso sorted de python, mezcla entre merge y insertion sort (TimSort) y slices a 5 primeras
urls = sorted(urls.iteritems(),key=lambda(k,v):(v,k),reverse=True)[:5]

for line in urls:
    print line
