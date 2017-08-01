from sys import argv;

script,from_file,to_file=argv;
open(to_file,'w').write(open(from_file,'r').read());

open(from_file).close();
open(to_file).close();
