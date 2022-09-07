import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

# def get_url(packet):
#     return packet[http.HTTPRequest].host + packet[http.HTTPRequest].path

# def get_login_info(packet):
#     if packet.haslayer(scapy.Raw):
#             load = packet(scapy.Raw).load
#             keywords = ['username','user','pass','login','password']
#             for keyword in keywords:
#                 if keyword in load:
#                     return load

def process_sniffed_packet(packet):
    # if packet.haslayer(http.HTTPRequest):
    #     url = get_url(packet)
    #     print("[+] HTTP Request >> " + url)
    #     login_info = get_login_info(packet)

    #     if login_info:
    #         print("\n\n[+] Possible username/password >>" + login_info + "\n\n")
    print(packet.show())
    print(packet.summary())
        

sniff('Wi-Fi')