import fire
import subprocess



def display_error(error):
    print("[-] Something was wrong")
    print("Err {}".format(error.decode()))
    exit(1)

        
def scan(target, ping=False):
    
    try:
        if ping:
            process = subprocess.Popen(["nmap", "-sT","-T4", "-p","21", "--open", target], stdout=subprocess.PIPE)
        else:
            process = subprocess.Popen(["nmap", "-P0", "-sT","-T4", "-p","21", "--open", target], stdout=subprocess.PIPE)

        output, error = process.communicate()
        if error:
            display_error(error)
    
        lines = output.decode().splitlines()
        for line in lines:
            if "open" in line and "ftp" in line:
                hprocess = subprocess.Popen(["hydra", "-l","anonymous","-p","anonymou@box.com","ftp://{}".format(target)], stdout=subprocess.PIPE)
                output, error = hprocess.communicate()
                if error:
                    display_error(error)
                h_lines = output.decode().splitlines()
                for hline in h_lines:
                    if "anonymous" in hline and "found" in hline:
                        print("{} ANONYMOUS FOUND".format(target))
                

    except FileNotFoundError:
        print("This script requires nmap and hydra")
    
if __name__ == '__main__':
    fire.Fire(scan)