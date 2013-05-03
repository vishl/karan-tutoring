import thread
import curses
import time
from threading import Lock


#globals
Scr = None
P = 12
Count = 0
mutex=Lock()
#functions
def init():
    global Scr 
    Scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    Scr.keypad(1)

def finish():
    curses.nocbreak()
    Scr.keypad(0)
    curses.echo()
    curses.endwin()

def atomicprint(row,column,string):
    mutex.acquire()

    Scr.addstr(row,column,string)
    mutex.release()


def counter():
    global Count
    global P
    Count=0
    while True:
        atomicprint(4,P, "Count = " + str(Count))
        Scr.refresh()
        Count+=1
        time.sleep(0.0001)


#Main program
init()

atomicprint(5,5,"Press q to quit")
Scr.refresh()
thread.start_new_thread(counter, ())

while True:
    n = Scr.getch()
    if(n<256):
        c = chr(n)
        
        atomicprint(6,5, "You pressed " + str(c))
        Scr.refresh()
        if c=='r':
            P=80
            atomicprint(4,12,  "            ")

            atomicprint(4,5,  "             ")
        if c=='l':
            P=5
            atomicprint(4,80,  "            ")
            atomicprint(4,12,  "            ")
            
        if c=='c':
            Count = 0
            atomicprint(4,80,  "             ")
            atomicprint(4,5,  "             ")
        if(c=="q"):
            break
    
finish()
