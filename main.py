import spsuml_manager
import packet_parser
import os


def parse_netowrks(yamlpath):
    import yaml
    with open(yamlpath) as yamlfile:
        networks = yaml.load(yamlfile)
    return networks


if __name__ == '__main__':
    # get packets
    pcappath = os.path.join('.', 'data', 'http.pcap')
    packets = packet_parser.parse(pcappath)

    # parse networks
    networks = parse_netowrks("./networks.yaml")

    # setup spsuml_manger
    manager = spsuml_manager.SpsumlManager(networks=networks)

    # fit networks
    manager.fit(packets)

    # select objects to preserve
    # manager.select(top_num=5)
