import os
import threading

HOST = input("What is the target? ")

def dns_recon(domain):
    '''This function will perform DNS related tools'''
    #os.system(f'amass enum -d {domain} -dir dns/amass_scan')
    #os.system(f'dnsenum {domain} > dns/dnsenum_output')
    os.system(f'subfinder -d {domain} -all -o dns/subfinder_output')

def probe():
    url_list = []
    with open("dns/subfinder_output") as f:
        for line in f:
            url_list.append(line.rstrip())
    os.system(f'httpx -l dns/subfinder_output -rl 5 -fc 404 -sc -location -server -o dns/httpx_output')






def main():
    current_dir = os.getcwd() # Get current working directory

    # Setup directories for the framework
    os.mkdir(f'{current_dir}/dns')
    os.mkdir(f'{current_dir}/network')
    os.mkdir(f'{current_dir}/spidering')
    dns_recon(HOST)
    probe()
#os.system("dnsrecon -d google.com)

if __name__ == '__main__':
    main()