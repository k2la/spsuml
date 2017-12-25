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

    def prioritize(self, datasets):
        rank = {}
        for name, dataset in datasets.items():
            for device_name, device in self.rnns.items():
                if name is device_name:
                    print("----- %s -----" % (name))
                    rank[device_name] = device["rnn"].evaluate(dataset["train"], dataset["test"])[0]
        print(rank)
        priorities = sorted(rank.items(), key=lambda x: x[1])
        priorities.reverse()
        # priorities = [name for _, p in enumerate(priorities)]
        return priorities
