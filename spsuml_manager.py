import spsuml
import preprocessor

class SpsumlManager:
    def __init__(self, networks):
        self.networks = networks["networks"]

    def setup_spsuml(self, feature_dim, time):
        self.spsuml = spsuml.Spsuml(networks=self.networks)
        self.spsuml.setup_rnns(feature_dim=feature_dim, time=time)

    def fit(self, dataset):
        self.spsuml.fit(dataset)

    def prioritize(self, packets, top_num=3):
        return self.spsuml.prioritize(packets)[:top_num]

    def preprocess(self, packets):
        network_dataset = {}
        # distribute
        for _, packet in enumerate(packets):
            for _, device in enumerate(self.networks):
                if device["ip"] in [packet.ip_src, packet.ip_dst]:
                    if not device["name"] in network_dataset: network_dataset[device["name"]] = []
                    network_dataset[device["name"]].append(packet.to_list())

        # packet2vec
        for name, data in network_dataset.items():
            network_dataset[name] = preprocessor.data2vec(data)

        # make train_data and test_data
        datasets = { name : {"train": [], "test": []} for name, _ in network_dataset.items()}
        for name, data in network_dataset.items():
            datasets[name]["train"], datasets[name]["test"] = preprocessor.dataset2LBdata(data, 10)
        return datasets
