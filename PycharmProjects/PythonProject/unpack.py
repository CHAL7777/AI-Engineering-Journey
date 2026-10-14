from curses.ascii import isupper

inn="CHaka"

def filtU(inn):
    liss=[]
    for i in inn:
        if isupper(i):
            liss.append(i)
    return  liss

ans=filtU(inn)

print(*ans)