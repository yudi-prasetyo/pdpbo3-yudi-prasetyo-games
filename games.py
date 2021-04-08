class Games():
    def __init__(self, nama, nama_dev, thn_rilis, platform, mode, pict = ""):
        self.nama = nama
        self.nama_dev = nama_dev
        self.thn_rilis = thn_rilis
        self.platform = platform
        self.mode = mode
        self.pict = pict

    def get_nama(self):
        return self.nama

    def get_nama_dev(self):
        return self.nama_dev

    def get_thn_rilis(self):
        return self.thn_rilis

    def get_platform(self):
        return self.platform

    def get_mode(self):
        return self.mode

    def get_pict(self):
        return self.pict