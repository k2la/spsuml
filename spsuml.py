import rnn


class Spsuml:
    def __init__(self, networks):
        self.networks = networks
        self.rnns = {}


    def setup_rnns(self, feature_dim, time):
        for _, device in enumerate(self.networks):
            self.rnns[device["name"]] = {
                "ip": device["ip"],
                "rnn": rnn.Rnn(feature_dim=feature_dim, time=time),
                "priority": 0
            }

    def fit(self, datasets):
        for name, dataset in datasets.items():
            for device_name, device in self.rnns.items():
                if name is device_name:
                    print("----- %s -----" % (name))
                    device["rnn"].fit(dataset["train"], dataset["test"])

    def prioritize(self, packets):
        return [i for i, v in enumerate(self.networks)]
