import rnn


class Spsuml:
    def __init__(self, networks):
        self.networks = networks
        self.rnns = {}
        self.setup_rnns()

    def setup_rnns(self):
        for _, device in enumerate(self.networks["networks"]):
            self.rnns[device["name"]] = {
                "ip": device["ip"],
                "rnn": rnn.Rnn(feature_size=5, time=10),
                "priority": 0
            }

    def fit(self, packets):
        pass

    def prioritize(self, packets):
        return [i for i, v in enumerate(self.networks["networks"])]
