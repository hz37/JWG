import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

client = udp_client.UDPClient('192.168.178.39', 31000)

while True:
    for idx in range(0, 100):
        msg = osc_message_builder.OscMessageBuilder(address = '/hey')
        msg.add_arg(idx)
        msg = msg.build()
        client.send(msg)
        print(idx)
        time.sleep(1)
    
