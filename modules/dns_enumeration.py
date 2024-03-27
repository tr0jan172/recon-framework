import os

def amass_scan(domain):
    '''Run an amass scan and save into a sqlite file'''
    pass

def dns_recon(domain):
    pass

def dns_enum():
    pass

def main():
    '''Main function for doing dns recon'''
    current_dir = os.getcwd()
    os.mkdir(f'{current_dir}/dns')
#os.system("dnsrecon -d google.com)