import spsuml_manager
import packet_parser
import os

if __name__ == '__main__':
    # get packets
    pcappath = os.path.join('.', 'data', 'http.pcap')
    packets = packet_parser.parse(pcappath)
    print(packets)

    # setup spsuml_manger
    manager = spsuml_manager.SpsumlManger

    # fit networks
    manager.fit()

    # select objects to preserve
    manager.select()