from .Diem import Diem


class Monhoc():
    diem: Diem
    def __init__(self,diem = None ,mamonhoc = None ,tenmonhoc = None ,sotinchi = None ):
        self.diem = diem
        self.mamonhoc = mamonhoc
        self.tenmonhoc = tenmonhoc
        self.sotinchi = sotinchi
    def checkdiem(self) -> Diem:
        return self.diem
    def checkClass(self):
        return "Monhoc"
