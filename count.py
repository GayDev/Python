def count(base, delay, limit):
    import time
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    anim = '|/-\\'          # [|][/][-][\]

    n = [0]
    a = 0
    while a < limit:
        s = ''
        for i in n[::-1]:
            s += digits[i]

        print(('[%s]\t' % anim[int(delay*a)%4]) + s,end='\r')
        #print(s)

        n[0] += 1
        n.append(0)
        if n[0] == base:
            for i in range(len(n)-1):
                if n[i] == base:
                    n[i] = 0
                    n[i+1] += 1

        if n[-1] == 0:
            n.pop()
        a += 1 
        #time.sleep(delay)


count(2,.000001,2**20)