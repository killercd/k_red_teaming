#!/usr/bin/python3
import fire
import subprocess



def display_error(output):
    print("[-] Something was wrong")
    print("Err {}".format(output.stderr))
    exit(1)

        
def scan(target, ping=False, verbose=False):
    
    try:
        if ping:
            output = subprocess.run("nmap -sT -T4 -p 21 -oG - --open {}".format(target), capture_output=True, shell=True, text=True)
        else:
            output = subprocess.run("nmap -P0 -sT -T4 -p 21 -oG - --open {}".format(target), capture_output=True, shell=True, text=True)
        
        if output.stderr:
            display_error(output)

        
        lines = output.stdout.splitlines()
        for line in lines:
            if "open" in line and "ftp" in line:
                ip = line.split(" ")[1]
                if verbose:
                    print("Ftp service found {}".format(ip))
                hprocess = subprocess.run("hydra -l anonymous -p anonymou@box.com ftp://{}".format(ip), capture_output=True, shell=True, text=True)
                if hprocess.stderr:
                    display_error(hprocess)
                
                h_lines = output.stdout.splitlines()
                for hline in h_lines:
                    if "anonymous" in hline and "found" in hline:
                        print("{} ANONYMOUS FOUND".format(target))
                

    except FileNotFoundError:
        print("This script requires nmap and hydra")
    
if __name__ == '__main__':
    fire.Fire(scan)