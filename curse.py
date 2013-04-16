import thread
import curses
import time

#globals
Scr = None

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

def counter():
    count=0
    while True:
        Scr.addstr(4,5, "Count = " + str(count))
        Scr.refresh()
        count+=1
        time.sleep(1)


#Main program
init()

Scr.addstr(5,5,"Press q to quit")
Scr.refresh()
thread.start_new_thread(counter, ())

while True:
    n = Scr.getch()
    if(n<256):
        c = chr(n)
        Scr.addstr(6,5, "You pressed " + str(c))
        Scr.refresh()
        if(c=="q"):
            break
    
finish()
