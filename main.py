import spsuml_manager
import packet_parser
import os

if __name__ == '__main__':
    # get packets
    pcappath = os.path.join('.', 'data', 'http.pcap')
    packets = packet_parser.parse(pcappath)

    # setup spsuml_manger
    manager = spsuml_manager.SpsumlManger

    # fit networks
    manager.fit(packets=packets)

    # select objects to preserve
    manager.select(top_num=5)