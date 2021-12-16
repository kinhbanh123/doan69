import pickle
from typing import List
from _Class.Data.Canhan import Canhan
from _Class.Data.Sinhvien import Sinhvien
from _Class.Data.Giaovien import Giaovien
from _Class.Data.Khoahoc import Khoahoc

from _Class.Data.Diem import Diem
from _Class.Data.Nganhdaotao import Nganhdaotao
from _Class.Data.Hedaotao import Hedaotao
from _Class.Data.Lophoc import Lophoc
#from Bus.wtf import quanlysv

class ip():
    def InputCanhan(i):
        inputHoten = input("hay nhap ho ten ")
        canhanList[i].hoten = inputHoten
        canhanList[i].macanhan = i
        canhanList[i].sdt = input("hay nhap sdt ")
        canhanList[i].quequan = input("hay nhap que quan ")
        canhanList[i].email = input("hay nhap email ")
        print(canhanList[i].outputInfo())
    def OutputCanhan(i):
        ff = open('./Doan2_DataB/canhan.txt','a+')
        ff.write(canhanList[i].hoten)
        ff.write("\n")
        ff.write(str(canhanList[i].macanhan))
        ff.write("\n")
        ff.write(canhanList[i].sdt)
        ff.write("\n")
        ff.write(canhanList[i].quequan)
        ff.write("\n")
        ff.write(canhanList[i].email)
        ff.write("\n")
        ff.close
    def InputSinhvien(i):
        inputHoten = input("hay nhap ho ten ")
        canhanList[i].hoten = inputHoten
        canhanList[i].macanhan = i
        canhanList[i].sdt = input("hay nhap sdt ")
        canhanList[i].quequan = input("hay nhap que quan ")
        canhanList[i].email = input("hay nhap email ")
        print(canhanList[i].outputInfo())
        sinhvienList[i].masinhvien = i
        sinhvienList[i].ngaysinh = input("hay nhap ngay sinh ") 
        sinhvienList[i].gioitinh = input("hay nhap gioi tinh ") 
        sinhvienList[i].diachi = input("hay nhap dia chi ")
        print(sinhvienList[i].masinhvien)
    def OutputSinhvien(i):
        ff = open('./Doan2/_DataB/sinhvien.txt','a+')
        ff.write(canhanList[i].hoten)
        ff.write("\n")
        ff.write(str(canhanList[i].macanhan))
        ff.write("\n")
        ff.write(canhanList[i].sdt)
        ff.write("\n")
        ff.write(canhanList[i].quequan)
        ff.write("\n")
        ff.write(canhanList[i].email)
        ff.write("\n")
        ff.write(str(sinhvienList[i].masinhvien))
        ff.write("\n")
        ff.write(sinhvienList[i].ngaysinh)
        ff.write("\n")
        ff.write(sinhvienList[i].gioitinh)
        ff.write("\n")
        ff.write(sinhvienList[i].diachi)
        ff.write("\n")
        ff.close
    def InputGiaovien(i):
        inputHoten = input("hay nhap ho ten ")
        canhanList[i].hoten = inputHoten
        canhanList[i].macanhan = i
        canhanList[i].sdt = input("hay nhap sdt ")
        canhanList[i].quequan = input("hay nhap que quan ")
        canhanList[i].email = input("hay nhap email ")
        print(canhanList[i].outputInfo())
        giaovienList[i].magiaovien = i
        giaovienList[i].ngaysinh = input("hay nhap ngay sinh ") 
        giaovienList[i].gioitinh = input("hay nhap gioi tinh ") 
        giaovienList[i].diachi = input("hay nhap dia chi ")
    def OutputGiaovien(i):
        ff = open('./Doan2/_DataB/giaovien.txt','a+')
        ff.write(canhanList[i].hoten)
        ff.write("\n")
        ff.write(str(canhanList[i].macanhan))
        ff.write("\n")
        ff.write(canhanList[i].sdt)
        ff.write("\n")
        ff.write(canhanList[i].quequan)
        ff.write("\n")
        ff.write(canhanList[i].email)
        ff.write("\n")
        ff.write(str(giaovienList[i].magiaovien))
        ff.write("\n")
        ff.write(giaovienList[i].ngaysinh)
        ff.write("\n")
        ff.write(giaovienList[i].gioitinh)
        ff.write("\n")
        ff.write(giaovienList[i].diachi)
        ff.write("\n")
        ff.close
    def InputKhoahoc(i):
        khoahocList[i].makhoahoc = i 
        khoahocList[i].tenkhoahoc = input("hay nhap ten khoa hoc ")


    def InputNganhdaotao(i):
        nganhdaotaoList[i].manganh = i
        nganhdaotaoList[i].tennganh = input("hay nhap ten nganh ")

    def InputDiem(i):
        diemList[i].diemtb = input("hay nhap diem tb ")
        diemList[i].diemthilan1 = input(" hay nhap diem thi lan thu 1 ")
        diemList[i].diemthilan2 = input(" hay nhap diem thi lan thu 2 ")
        diemList[i].hocky = input("hay nhap diem hoc ky ")
        diemList[i].diemtbc = (int(diemList[i].diemthilan1) + int(diemList[i].diemthilan2) + int(diemList[i].hocky)*3)/5


canhanList = [Canhan() for i in range (0,1000)]
sinhvienList =[Sinhvien() for i in range (0,1000)]
giaovienList = [Giaovien() for i in range (0,1000)]
khoahocList = [Khoahoc() for i in range (0,1000)]
nganhdaotaoList = [Nganhdaotao() for i in range (0,1000)]
diemList = [Diem() for i in range (0,1000)]


class quanlysv():
    def findsinhvien(self):
        print("hay nhap ma sinh vien")
        n = int(input())
        print(canhanList[n].hoten)
    def hienthithongtin(self):
        print(canhanList[i].outputInfo)
        print(sinhvienList[i].outputInfo)
    def xuatthongtin(i):
        print("hay nhap ten file can xuat ")
        tenfile = input()
        f = open(tenfile,'a+')
        f.write(canhanList[i].outputInfo())
        f.write("\n")
        f.write(sinhvienList[i].outputInfo())

class quanlygv():
    def findgiaovien(self):
        print("hay nhap ma giao vien")
        n = int(input())
        print(canhanList[n].hoten)
    def hienthithongtin(self):
        print(canhanList[i].outputInfo)
        print(giaovienList[i].outputInfo)
    def xuatthongtin(i):
        print("hay nhap ten file can xuat ")
        tenfile = input()
        f = open(tenfile,'a+')
        f.write(canhanList[i].outputInfo())
        f.write("\n")
        f.write(giaovienList[i].outputInfo())
def docdata():
    ff = open("./Doan2/_DataB/sinhvien.txt",'r+')
    hotenn ="text"
    while hotenn != "":
        hotenn = ff.readline()
        ii = ff.readline()
        canhanList[ii].hoten = hotenn
        canhanList[ii].macanhan = ii
        canhanList[ii].sdt = ff.readline()
        canhanList[ii].quequan = ff.readline()
        canhanList[ii].email = ff.readline()
        sinhvienList[ii].masinhvien = ff.readline()
        sinhvienList[ii].ngaysinh = ff.readline()
        sinhvienList[ii].gioitinh = ff.readline()
        sinhvienList[ii].diachi = ff.readline()
        ii = ii+1
 ################################################################## Main ################################################
if __name__ == '__main__':
    tuychon = "open"
    ii = 0
    ee = open("./Doan2/_DataB/i.txt",'r+')
    i = int(ee.readline())
    docdata 
    while tuychon != "close":
        print("Ban muon thuc hien gi (0 neu muon tat)")
        print("1 de nhap ten sinh vien ")
        print("2 de nhap ten giao vien ")
        print("3 de nhap ten khoa hoc ")
        print("4 de nhap nganh dao tao ")
        print("5 de nhap diem ")
        print("6 de luu du lieu ")
        ttcheck = int(input())
        if ttcheck == 0:
            tuychon = "close"
        if ttcheck == 1:
            ip.InputSinhvien(i)
        if ttcheck == 2:
            ip.InputGiaovien(i)
        if ttcheck == 3 :
            ip.InputKhoahoc(i)
        if ttcheck == 4:
            ip.InputNganhdaotao(i)
        if ttcheck ==5:
            print("hay nhap ma sinh vien de nhap diem")
            mas = int(input())
            ip.InputDiem(mas)
        if ttcheck ==6:
            print("1 de sinh vien 2 de giao vien ")
            ttcheck2 =int(input())
            if ttcheck2 == 1:
                for o in range(len(sinhvienList)):
                    if sinhvienList[o].masinhvien != "":
                        ip.OutputSinhvien(o)
            if ttcheck2 ==2:
                for o in range(len(giaovienList)):
                    if giaovienList[o].magiaovien != "":
                        ip.OutputGiaovien(o)
        if ttcheck == 7:
            print(canhanList[1].hoten)
        i = i+1


