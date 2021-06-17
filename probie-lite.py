
import sys
import time
from datetime import datetime
from OuiLookup import OuiLookup
from scapy.all import *
from termcolor import colored


def process_packet(packet):
    PROBE_REQUEST_TYPE = 0
    PROBE_REQUEST_SUBTYPE = 4
    if packet.haslayer(Dot11):
        if packet.type==PROBE_REQUEST_TYPE and packet.subtype == PROBE_REQUEST_SUBTYPE:
            PrintPacket(packet)


def hex_to_binary(hex_code):
    bin_code = bin( hex_code )[2:]
    padding = (4-len(bin_code)%4)%4
    final = '0'*padding + bin_code
    if len(final) != 8:
        final = '0'*4+final
    return final

def getVendor(mac):
    v = OuiLookup().query(mac)
    try:
        for key,value in v[0].items():
            vendor = value
        return vendor
    except:
        return "error"

def getbinary(mac):
    n = []
    n = mac.split(':')
    binary = ''

    for i in n:
        bin_arr = hex_to_binary(int(i,16))
        binary = binary+str(bin_arr)
    return binary


def getsecleastbit(mac):

    binary = getbinary(mac)
    secleastbit = str(binary)[6]   
    return secleastbit

def is_anonymous(slb):
    if slb:
        return "LAA"
    return "UAA"

def PrintPacket(pkt):
    logfile = "./log.csv"

    try:
        rssi =  pkt.dBm_AntSignal
    except:
        rssi = -100
    
    pkt_time = pkt.time
    time_val = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(pkt.time))
    

    dst = pkt.addr3
    src = pkt.addr2
    secleastbit = getsecleastbit(src)
    ssid = pkt[Dot11ProbeReq].info
    src_binary = getbinary(src)
    dst_binary = getbinary(dst)
    src_vendor = getVendor(src)
    dst_vendor = getVendor(dst)
    anon = is_anonymous(int(secleastbit))

    try:
        channel = pkt[Dot11EltDSSSet].channel
    except:
        channel = 0
    if ssid.decode("utf-8") == '':
        ssid = b''


    out=("Time: %s  Source: %s Anonymous: %s Dest: %s SSID: %s Channel: %d RSSi: %d "%(time_val,src,anon,dst,ssid.decode("utf-8"),channel,rssi))
    print(colored(out,'green'))


    entry = "%s,%s,%s,%d,%d,%s,%s,%s,%s,%s,%s,%s\n"%(pkt_time,time_val,ssid.decode("utf-8"),channel,rssi,src,src_binary,secleastbit,src_vendor,dst,dst_binary,dst_vendor)
    
    f= open(logfile,"a")
    f.write(entry)
    f.close()
    


def main():

    banner = '''
        _____           _     _       __             __
       |  __ \         | |   (_)      \ \           / /
       | |__) | __ ___ | |__  _  ___   \ \   ___   / / 
       |  ___/ '__/ _ \| '_ \| |/ _ \   \ \ / _ \ / /  
       | |   | | | (_) | |_) | |  __/    \ \ (_) / /   
       |_|   |_|  \___/|_.__/|_|\___|     \_\___/_/  
       By: ⚡serialwaffle ⚡
    '''
    os.system('clear')
    print(colored(banner,'cyan'))
    

    interface = sys.argv[1]
    print("using %s"%interface)



    sniff(iface=interface, prn=process_packet)
    
    while (True):
        pass



if __name__ in '__main__':
    main()

