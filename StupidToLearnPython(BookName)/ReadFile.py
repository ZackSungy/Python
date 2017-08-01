from sys import argv;

sctipt,filename=argv;
print "Now we'are open this %r"%filename;
print "If you don't want that,hit CTRL-C(^C)";
print "If you do want that,hit Enter.";

raw_input("?");
print "Opening the file...";

target=open(filename,'r');
while True:
    line=target.readline();
    if len(line)==0:
        break;
    print line,

target.close();
