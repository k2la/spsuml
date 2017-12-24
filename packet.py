class Packet:
    def __init__(self, ip_src, ip_dst, proto, src_size, dst_size):
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        self.proto = proto
        self.src_size = src_size
        self.dst_size = dst_size