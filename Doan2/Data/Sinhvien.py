from .Canhan import Canhan

class Sinhvien(Canhan):
    def __init__(self,hoten = "" ,sdt = "" ,quequan = "" ,email = "" ,masinhvien = "" ,ngaysinh = "" ,gioitinh = "" ,diachi = "" ):
        Canhan.__init__(self,hoten,sdt,quequan,email)
        self.masinhvien = masinhvien
        self.ngaysinh = ngaysinh
        self.gioitinh = gioitinh
        self.diachi = diachi
    def outputInfo(self):
        return f"Masinhvien: {self.masinhvien} Ngaysinh: {self.ngaysinh} Gioitinh: {self.gioitinh} Diachi: {self.diachi}"
    def checkClass(self):
        return "Sinhvien"