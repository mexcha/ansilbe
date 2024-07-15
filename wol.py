import socket
import binascii

def enviar_magic_packet(mac_address, ip_address, puerto=9):
    
    mac_hex = mac_address.replace(':', '').replace('-', '')
    mac_bytes = binascii.unhexlify(mac_hex)
    magic_packet = b'\xff' * 6 + mac_bytes * 16
   
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(magic_packet, (ip_address, puerto))
        print("Magic Packet enviado con éxito a", mac_address)
    
    except Exception as e:
        print("Error al enviar el Magic Packet:", e)


direccion_mac = '1c:69:7a:0c:fa:af'  
direccion_ip = '10.101.42.25'
enviar_magic_packet(direccion_mac, direccion_ip)