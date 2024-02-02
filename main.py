def openFile(file_path):
    with open(file_path) as f:
        return f.read()

def wc(f):
    return (f'There are {len(f.split())} words in the book!')

def lc(f):
    d={}
    for line in f:
        i=0
        while i < len(line):
            if line[i].isalpha():
                if line[i].lower() not in d:
                    d[line[i].lower()]=1
                else:
                    #print('hi')
                    d[line[i].lower()]+=1
            i+=1

    return d
def sorttest(d):
    return d['number']
def sortem(d):
    L=[]
    for i,j in d.items():
        L.append({'character:':i,'number':j})
    L.sort(reverse=True, key=sorttest)
    return L

def main():
    f=openFile('./books/testbook.txt')
    print(wc(f))
    g=lc(f)
    print(sortem(g))
main()