class Spsuml:
    def __init__(self):
        self.networks = []

    def setup_netowrks(self, yamlpath):
        import yaml
        with open(yamlpath) as yamlfile:
            networks = yaml.load(yamlfile)
        self.networks = networks