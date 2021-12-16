from typing import List

from .Khoahoc import Khoahoc
from .Nganhdaotao import Nganhdaotao
from .Hedaotao import Hedaotao
from .Sinhvien import Sinhvien
from .Giaovien import Giaovien



class Lophoc():
    khoahoc: Khoahoc
    nganhdaotao: Nganhdaotao
    hedaotao: Hedaotao
    sinhvien: List[Sinhvien]
    giaovien: List[Giaovien]
    def __init__(self,nganhdaotao,hedaotao,khoahoc):
        self.nganhdaotao = nganhdaotao
        self.hedaotao = hedaotao
        self.khoahoc = khoahoc
        self.sinhvien = []
        self.giaovien = []
    def addsinhvien(self,name:Sinhvien):
        self.sinhvien.append(name)
    def checksinhvien(self) -> List[Sinhvien]:
        return self.sinhvien
    def addgiaovien(self,name:Giaovien):
        self.giaovien.append(name)
    def checkgiaovien(self) -> List[Giaovien]:
        return self.giaovien
    def checkhedaotao(self) -> Hedaotao:
        return self.hedaotao
    def checkhoahoc(self) -> Khoahoc:
        return self.khoahoc
    def checknganhdaotao(self) -> Nganhdaotao:
        return self.nganhdaotao
    def checkClass(self):
        return "Lophoc"