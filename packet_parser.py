import packet
import pcap2csv
import pandas as pd
import os

def parse(filepath):
    pcap2csv.pcap2csv(filepath)
    csvpath = os.path.join('.', 'data', 'packets.csv')
    packet_df = pd.read_csv(csvpath)
    packets = []
    for _, packet_entry in enumerate(packet_df.iterrows()):
        p = packet.Packet(
            ip_src=packet_entry[1].ip_src,
            ip_dst=packet_entry[1].ip_dst,
            proto=packet_entry[1].ip_proto,
            src_size=100,
            dst_size=100,
        )
        packets.append(p)
    return packets
