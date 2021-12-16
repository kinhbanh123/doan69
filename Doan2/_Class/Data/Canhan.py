class Canhan:
    def __init__(self,hoten = "",sdt = "" ,quequan = "" ,email = "" ,macanhan = ""):
        self.hoten = hoten
        self.macanhan = macanhan
        self.sdt = sdt
        self.quequan = quequan
        self.email = email
    def outputInfo(self):
        return f"hoten: {self.hoten} sdt: {self.sdt} quequan: {self.quequan} email: {self.email}"
    def checkClass(self):
        return "Canhan"