from .Sinhvien import Sinhvien
from .Giaovien import Giaovien
from .Canhan import Canhan

# class Khoahoc():
#     def __init__(self,makhoahoc = None ,tenkhoahoc = None ):
#         self.makhoahoc = makhoahoc
#         self.tenkhoahoc = tenkhoahoc
#     def checkClass(self):
#         return "Khoahoc"

# class Nganhdaotao():
#     def __init__(self,manganh = None ,tennganh = None ):
#         self.manganh = manganh
#         self.tennganh = tennganh
#     def checkClass(self):
#         return "Nganhdaotao"

# class Hedaotao():
#     def __init__(self,mahedaotao = None ,tenhedaotao = None ):
#         self.mahedaotao = mahedaotao
#         self.tenhedaotao = tenhedaotao
#     def checkClass(self):
#         return "Hedaotao"

# class Lophoc():
#     khoahoc: Khoahoc
#     nganhdaotao: Nganhdaotao
#     hedaotao: Hedaotao
#     sinhvien: List[Sinhvien]
#     giaovien: List[Giaovien]
#     def __init__(self,nganhdaotao,hedaotao,khoahoc):
#         self.nganhdaotao = nganhdaotao
#         self.hedaotao = hedaotao
#         self.khoahoc = khoahoc
#         self.sinhvien = []
#         self.giaovien = []
#     def addsinhvien(self,name:Sinhvien):
#         self.sinhvien.append(name)
#     def checksinhvien(self) -> List[Sinhvien]:
#         return self.sinhvien
#     def addgiaovien(self,name:Giaovien):
#         self.giaovien.append(name)
#     def checkgiaovien(self) -> List[Giaovien]:
#         return self.giaovien
#     def checkhedaotao(self) -> Hedaotao:
#         return self.hedaotao
#     def checkhoahoc(self) -> Khoahoc:
#         return self.khoahoc
#     def checknganhdaotao(self) -> Nganhdaotao:
#         return self.nganhdaotao
#     def checkClass(self):
#         return "Lophoc"
       
# class Diem():
#     def __init__(self,diemtb = None ,diemthilan1 = None ,diemthilan2 = None ,diemtbc = None ,hocky = None ):
#         self.diemtb = diemtb
#         self.diemthilan1 = diemthilan1
#         self.diemthilan2 = diemthilan2
#         self.diemtbc = diemtbc
#         self.hocky = hocky
#     def checkClass(self):
#         return "Diem"
 
# class Monhoc():
#     diem: Diem
#     def __init__(self,diem = None ,mamonhoc = None ,tenmonhoc = None ,sotinchi = None ):
#         self.diem = diem
#         self.mamonhoc = mamonhoc
#         self.tenmonhoc = tenmonhoc
#         self.sotinchi = sotinchi
#     def checkdiem(self) -> Diem:
#         return self.diem
#     def checkClass(self):
#         return "Monhoc"
