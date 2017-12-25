import spsuml_manager
import packet_parser
import os


def parse_yaml(yamlpath):
    import yaml
    with open(yamlpath) as yamlfile:
        data = yaml.load(yamlfile)
    return data


def load_env():
    from dotenv import load_dotenv
    from os.path import join, dirname
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


if __name__ == '__main__':
    load_env()

    # get packets
    pcappath = os.path.join('.', 'data', 'http.pcap')
    packets = packet_parser.parse(pcappath)

    # parse networks
    networks = parse_yaml(os.environ.get("NETWORKS_YAML"))

    # setup spsuml_manger
    manager = spsuml_manager.SpsumlManager(networks=networks)
    manager.setup_spsuml(feature_dim=5, time=10)

    # fit networks
    preprocessed_packets = manager.preprocess(packets=packets)
    manager.fit(dataset=preprocessed_packets)

    # select objects to preserve
    priorities = manager.prioritize(packets=packets, top_num=5)
    print(priorities)
