import spsuml


class SpsumlManager:
    def __init__(self, networks):
        self.spsuml = spsuml.Spsuml(networks)

    def fit(self, packets):
        self.spsuml.fit(packets)

    def prioritize(self, packets, top_num=3):
        return self.spsuml.prioritize(packets)[:top_num]

    def preprocess(self):
        pass