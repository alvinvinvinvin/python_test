import turtle, sys, math
bob = turtle.Turtle()
print(bob)

def square(bob, length):
    bob.pd()
    for _ in range(4):
        bob.fd(length)
        bob.lt(90)
    bob.pu()
    #bob.mainloop()
    #bob.done()


#square(bob,200)

def polygon(bob, length, n, a):
    bob.pd()
    for _ in range(n):
        bob.fd(length)
        bob.lt(a/n)
    bob.pu()

#polygon(bob, 120, 9)

def crcle(t, r, length):
    n = (2*math.pi*r)/length
    polygon(t, length, int(n), 360)

def arc(t, r, l, a):
    n = ((a/360.0)*(2*math.pi*r))/l
    polygon(t, l, int(n), a)

def main():
    '''
    n = sys.argv[1]
    polygon(bob, 120, int(n))
    '''
    r = sys.argv[1]
    l = sys.argv[2]
    a = sys.argv[3]
    arc(bob, int(r), int(l), int(a))
if __name__ == "__main__":
    main()
