from sys import exit;
HP=3;
bag=[];
times=0;
deadgod=0;
Monster=0;
potions=True;
print "Welcome to the game.";

def GameStart():
    global HP
    global bag
    global deadgod
    global Monster
    global potions
    global times;
    again=',';
    if times>0:
        again=' again? ';
    times+=1;
    print "If you want to play%shit Enter please.\nIf you don't want to play,hit CTRL-C(^C)."%again;
    raw_input(">");
    print """You have three health points.
You have a empty bag.
Now begin your adventure.
And you can hit 'RETURN' to return last room.\n
"""
    HP=3;
    bag=[];
    deadgod=0;
    Monster=0;
    potions=True;
    Start();

def GameOver(reason):
    print 'Because %s,You dead!\n'%reason;
    GameStart();

def monster():
    global HP;     
    if 'stick' in bag:
        HP-=1;
        print ('\nYou fight monsters.HP-1');
        if HP==0:
            GameOver('the HP is 0');
    else:
        GameOver('killed by a monster');

def Dead_God():
    global HP;
    global deadgod;
    print 'You see the dead god!fighting or run.';
    choose=raw_input('>');
    if choose=='fighting':
        if deadgod>0:
            GameOver('The dead god gets pissed off!Kill you!');
        else:
            print '\nDead god admire your courage! HP+1';
            HP+=1;
            deadgod+=1;
            Second();
    elif choose=='run':
        Second();
    else:
        print '\nNo such operation!';
        Dead_God();
    

def second_left():
    if 'knife' in bag:
        if 'torch' in bag:
            Third();
        else:
            print '\nIs very dark.\ngo?';
            choose=raw_input('>');
            if choose=='go':
                Dead_God();
            elif choose=='RETURN':
                Second();
            else:
                print '\nNo such operation!'
                second_left();
    else:
        print "\nThere's a boat here, but it's tied up with ropes";
        Second();
        

def second_right():
    global Monster;
    print "\nThere are three rooms ahead of you.Please choose";
    print 'left or right or middle';
    choose=raw_input('>');
    if choose=='left' and 'torch' in bag:
        print '\nThe room is emtpy!Return to the room!';
        second_right();
    elif choose=='middle' and 'knife' in bag:
        print '\nThe room is emtpy!Return to the room!';
        second_right();
    elif choose=='right' and Monster>0:
        print '\nThe room is emtpy!Return to the room!';
        second_right();
    elif choose=='left':
        monster();
        bag.append('torch');
        print '\nYou get the torch!Return the room!';
        second_right();
    elif choose=='right':
        monster();
        Monster=1;
        print 'Return the room!';
        second_right();
    elif choose=='middle':
        bag.append('knife');
        print '\nYou get the knife!Return the room!';
        second_right();
    elif choose=='RETURN':
        Second();
    else:
        print '\nNo such operation!'
        second_right();

def Start():
    print "\nYou are in First room!"
    print "There are two rooms ahead of you.Please choose";
    print 'left or right';
    choose=raw_input('>');
    if choose=='left' and 'key' in bag:
        print 'The room is emtpy!Return to the room!';
        Start();
    elif choose=='right' and 'stick' in bag:
        Second();
    elif choose=='left':
        monster();
        bag.append('key');
        print '\nYou get the key!Return the room';
        Start();
    elif choose=='right':
        bag.append('stick');
        print '\nYou get the stick!';
        Second();
    else:
        print '\nNo such operation!'
        Start();

def Second():
    print "\nYou are in Second room!"
    print "There are two door ahead of you.Please choose";
    print 'left or right';
    choose=raw_input('>');
    if 'key' in bag:
        if choose=='left':
            second_left();
        elif choose=='right':
            second_right();
        else:
            print '\nNo such operation!'; 
            Second();
    elif choose=='RETURN':
        Start();    
    elif choose=='left' or choose=='right':
        print '\nYou have no key!';
        Second();
    else:
        print '\nNo such operation!'; 
        Second();
        
def Third():
    global HP;
    global times;
    global potions;
    print "\nYou are in Third room";
    print "There are three rooms ahead of you.";
    print 'There have a big boss in one of the rooms.';
    print 'The room monster will renascence.please choose';
    print 'left or right or middle';
    choose=raw_input('>');
    if choose=='left':
        monster();
        if potions:
            HP=3;
            print ('You get the Potions,Your HP is 3.')
            points=False;
        print 'Return the room';
        Third();
    elif choose=='middle':
        if HP==3:
            print "Congratulations on your customs clearance!";
            print "The number of times you use is %d"%times;
            exit(0);
        else:
            GameOver('you meet the boss!And he kill you!');
    elif choose=='right':
        monster();
        print 'Return the room';
        Third();
    elif choose=='RETURN':
        Second();
    else:
        print '\nNo such operation!'; 
        Third();
        

GameStart();
