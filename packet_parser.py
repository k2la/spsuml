import packet
import pcap2csv
import pandas as pd


# data_path = os.path.join('.', 'data', '10.144.0.0-2017-11-17-1300.pcap')
# pcap2csv(data_path)

def parse(filepath):
    pcap2csv.pcap2csv(filepath)
    packet_df = pd.read_csv(filepath)
    packets = []
    for packet_entry in enumerate(packet_df):
        p = packet.Packet(
            ip_src=packet_entry.ip_src,
            ip_dst=packet_entry.ip_dst,
            proto=packet_entry.ttl,
            src_size=100,
            dst_size=100,
        )
        packets.append(p)
    return packets
