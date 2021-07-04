#importstuff


#lees bestand
file1 = open('/home/meijeoppenhuizen/PycharmProjects/GRAFRECHT/GRAFRECHT.dat','r' )

Lines = file1.readlines()
#print(file1)

count = 0

#definieer recordtypes
record00 = dict(RECORDTYPE=0, GH="GH", gemeentenaam="Zeist")
record10 = dict(RECORDTYPE=10)
record20 = dict(RECORDTYPE=20)
record21 = dict(RECORDTYPE=21)


#parse regels
def slices(s, *args):
    position = 0
    for length in args:
        return s[position:position + length]
        position += length


# Strips the newline character
for line in Lines:
    print(line)
    count += 1
    linerec = slices(line,2)
    print("Linerec:",linerec)
    if linerec == '10':
        print("10-record")
    else:    print('mislukt')

#afsluiten
#file1.close()