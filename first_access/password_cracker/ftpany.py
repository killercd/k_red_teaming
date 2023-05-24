import fire
import subprocess



def scan(target):
    
    try:
        process = subprocess.Popen(["nmap", "-sV", "-p 21", "--open", target], stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output.decode())

    except FileNotFoundError:
        print("This script requires nmap")
    
if __name__ == '__main__':
    fire.Fire(scan)