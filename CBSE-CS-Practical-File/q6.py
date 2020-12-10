with open('source.txt', 'r') as fh:
    s=fh.readlines()
    linecount=len(s)
    b=""
    for i in range(0, linecount):
        a=s[i]
        if a[0]!='@':
            b=b+a
        
    with open('target.txt', 'w') as fh2:
        fh2.write(b)