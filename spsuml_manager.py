import spsuml


class SpsumlManager:
    def __init__(self, networks):
        self.spsuml = spsuml.Spsuml(networks)

    def fit(self, packets):
        self.spsuml.fit(packets)

    def select(self, top_num=3):
        return self.spsuml.select[:top_num]
