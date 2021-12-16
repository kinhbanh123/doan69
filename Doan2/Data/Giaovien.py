from .Canhan import Canhan
class Giaovien(Canhan):
    def __init__(self,hoten = "" ,sdt = "" ,quequan = "" ,email = "" ,magiaovien = "" ,gioitinh = "" ,ngaysinh = "" ,diachi = "" ):
        Canhan.__init__(self,hoten,sdt,quequan,email)
        self.magiaovien = magiaovien
        self.ngaysinh = ngaysinh
        self.gioitinh = gioitinh
        self.diachi = diachi
    def checkClass(self):
        return "Giaovien"
    def outputInfo(self):
        return f"Magiaovien: {self.magiaovien} Ngaysinh: {self.ngaysinh} Gioitinh: {self.gioitinh} Diachi: {self.diachi}"