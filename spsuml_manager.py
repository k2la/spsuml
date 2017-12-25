import spsuml


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
        dataset = {}
        #
        for _, packet in enumerate(packets):
            for _, device in enumerate(self.networks):
                if device["ip"] in [packet.ip_src, packet.ip_dst]:
                    if not device["name"] in dataset: dataset[device["name"]] = []
                    dataset[device["name"]].append(packet)
        return dataset
