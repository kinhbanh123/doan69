import pickle
from typing import List
from _Class.Data.Canhan import Canhan
from _Class.Data.Sinhvien import Sinhvien
from _Class.Data.Giaovien import Giaovien
from _Class.Data.Khoahoc import Khoahoc
from _Class.Data.Monhoc import Monhoc
from _Class.Data.Diem import Diem
from _Class.Data.Nganhdaotao import Nganhdaotao
from _Class.Data.Hedaotao import Hedaotao
from _Class.Data.Lophoc import Lophoc
#from Bus.wtf import quanlysv

class ip():
    def InputCanhan(i):
        inputHoten = input("hãy nhập họ tên ")
        canhanList[i].hoten = inputHoten
        canhanList[i].macanhan = i
        canhanList[i].sdt = input("hãy nhập sdt ")
        canhanList[i].quequan = input("hãy nhập quê quán ")
        canhanList[i].email = input("hãy nhập email ")
        print(canhanList[i].outputInfo())
    def OutputCanhan(i):
        ff = open('_DataB/canhan.txt','a+', encoding='utf-8')
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
        inputHoten = input("hãy nhập họ tên ")
        canhanList[i].hoten = inputHoten
        canhanList[i].macanhan = i
        canhanList[i].sdt = input("hãy nhập sdt ")
        canhanList[i].quequan = input("hãy nhập quê quán ")
        canhanList[i].email = input("hãy nhập email ")
        print(canhanList[i].outputInfo())
        sinhvienList[i].masinhvien = i
        sinhvienList[i].ngaysinh = input("hãy nhập ngay sinh ") 
        sinhvienList[i].gioitinh = input("hãy nhập gioi tinh ") 
        sinhvienList[i].diachi = input("hãy nhập dia chi ")
        print(sinhvienList[i].masinhvien)
    def OutputSinhvien(i):
        ff = open('_DataB/sinhvien.txt','a+', encoding='utf-8')
        ff.write(str(canhanList[i].macanhan))
        ff.write("\n")
        ff.write(canhanList[i].hoten)
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
        inputHoten = input("hãy nhập họ tên ")
        canhanList[i].hoten = inputHoten
        canhanList[i].macanhan = i
        canhanList[i].sdt = input("hãy nhập sdt ")
        canhanList[i].quequan = input("hãy nhập quê quán ")
        canhanList[i].email = input("hãy nhập email ")
        print(canhanList[i].outputInfo())
        giaovienList[i].magiaovien = i
        giaovienList[i].ngaysinh = input("hãy nhập ngay sinh ") 
        giaovienList[i].gioitinh = input("hãy nhập gioi tinh ") 
        giaovienList[i].diachi = input("hãy nhập dia chi ")
    def OutputGiaovien(i):
        ff = open('_DataB/giaovien.txt','a+', encoding='utf-8')
        ff.write(str(canhanList[i].macanhan))
        ff.write("\n")
        ff.write(canhanList[i].hoten)
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
        khoahocList[i].tenkhoahoc = input("hãy nhập ten khoa hoc ")
    def OutputKhoahoc(i):
        link = '_DataB/_khoahoc/' + str(khoahocList[i].tenkhoahoc) +'.txt'
        ff = open(link,'a+', encoding='utf-8')
        ff.close
        linkk = '_DataB/_khoahoc/' + str(khoahocList[i].tennganh) +' thong tin'+'.txt'
        fff = open(linkk,'a+', encoding='utf-8')
        fff.close
    def AddsvKhoahoc(i):
        link = '_DataB/_nganhhoc/' + str(khoahocList[i].tenkhoahoc) +'.txt'
        ff = open(link,'a+', encoding='utf-8')
        check = "off"
        while check == "off": 
            print("hãy nhập mã sinh viên để add vào khoá học ")
            ff.write(input())
            ff.write("\n")
            print("bấm số 0 để exit, hoặc ấn phím khác để tiếp tục add ")
            check = input()
            if check == "0":
                check = "onl"
            else:
                check = "off"
        ff.close

    def InputNganhdaotao(i):
        nganhdaotaoList[i].manganh = i
        nganhdaotaoList[i].tennganh = input("hãy nhập ten nganh ")
    def OutputNganhdaotao(i):
        link = '_DataB/_nganhhoc/' + str(nganhdaotaoList[i].tennganh) +'.txt'
        ff = open(link,'a+', encoding='utf-8')
        ff.close
        linkk = '_DataB/_nganhhoc/' + str(nganhdaotaoList[i].tennganh) +' thong tin'+'.txt'
        fff = open(linkk,'a+', encoding='utf-8')
        fff.close
    def AddsvNganh(i):
        link = '_DataB/_nganhhoc/' + str(nganhdaotaoList[i].tennganh) +'.txt'
        ff = open(link,'a+', encoding='utf-8')
        check = "off"
        while check == "off": 
            print("hãy nhập mã sinh viên để add vào ngành ")
            ff.write(input())
            ff.write("\n")
            print("bấm số 0 để exit, hoặc ấn phím khác để tiếp tục add ")
            check = input()
            if check == "0":
                check = "onl"
            else:
                check = "off"
        ff.close
        
    def InputDiem(i):
        diemList[i].diemtb = input("hãy nhập điểm tb ")
        diemList[i].diemthilan1 = input(" hãy nhập điểm thi lần thứ 1 ")
        diemList[i].diemthilan2 = input(" hãy nhập điểm thi lần thứ 2 2 ")
        diemList[i].hocky = input("hãy nhập điểm học kỳ ")
        diemList[i].diemtbc = (int(diemList[i].diemthilan1) + int(diemList[i].diemthilan2) + int(diemList[i].hocky)*3)/5
    def OutputDiem(i):
        ff = open('_DataB/diem.txt','a+', encoding='utf-8')
        ff.write(canhanList[i].macanhan)
        ff.write("\n")
        ff.write(canhanList[i].hoten)
        ff.write("\n")
        ff.write(diemList[i].diemtb)
        ff.write("\n")
        ff.write(diemList[i].diemthilan1)
        ff.write("\n")
        ff.write(diemList[i].diemthilan2)
        ff.write("\n")
        ff.write(diemList[i].hocky)
        ff.write("\n")
        ff.write(str(diemList[i].diemtbc))
        ff.write("\n")
        ff.close

    def InputMonhoc(i):
        monhocList[i].mamonhoc = i
        monhocList[i].tenmonhoc = input("hãy nhập tên môn học ")
        monhocList[i].sotinchi = input("hãy nhập số tín chỉ ")
    def OutputMonhoc(i):
        pass
class quanlymonhoc():
    pass

class quanlysv():
    def findsinhvien():
        print("hãy nhập mã sinh viên")
        n = int(input())
        print(canhanList[n].hoten)
    def hienthithongtin(self):
        print(canhanList[i].outputInfo)
        print(sinhvienList[i].outputInfo)
    def xuatthongtin(i):
        print("hãy nhập ten file can xuat ")
        tenfile = input()
        f = open(tenfile,'a+')
        f.write(canhanList[i].outputInfo())
        f.write("\n")
        f.write(sinhvienList[i].outputInfo())
    def docdatasv():
        ff = open("_DataB/sinhvien.txt",'r+', encoding='utf-8')
        check ="text"
        luot = 1
        while check != "":
            if luot == 2:
                ii = int(check)
                canhanList[ii].hoten = ff.readline()
                canhanList[ii].macanhan = ii
                canhanList[ii].sdt = ff.readline()
                canhanList[ii].quequan = ff.readline()
                canhanList[ii].email = ff.readline()
                sinhvienList[ii].masinhvien = ff.readline()
                sinhvienList[ii].ngaysinh = ff.readline()
                sinhvienList[ii].gioitinh = ff.readline()
                sinhvienList[ii].diachi = ff.readline()
                check = ff.readline()
            else:
                ii = int(ff.readline())
                canhanList[ii].hoten = ff.readline()
                canhanList[ii].macanhan = ii
                canhanList[ii].sdt = ff.readline()
                canhanList[ii].quequan = ff.readline()
                canhanList[ii].email = ff.readline()
                sinhvienList[ii].masinhvien = ff.readline()
                sinhvienList[ii].ngaysinh = ff.readline()
                sinhvienList[ii].gioitinh = ff.readline()
                sinhvienList[ii].diachi = ff.readline()
                check = ff.readline()
                luot = luot + 1

class quanlygv():
    def findgiaovien():
        print("hãy nhập mã giáo viên")
        n = int(input())
        print(canhanList[n].hoten)
    def hienthithongtin():
        print(canhanList[i].outputInfo)
        print(giaovienList[i].outputInfo)
    def xuatthongtin(i):
        print("hãy nhập ten file can xuat ")
        tenfile = input()
        f = open(tenfile,'a+')
        f.write(canhanList[i].outputInfo())
        f.write("\n")
        f.write(giaovienList[i].outputInfo())
    def docdatagv():
        ff = open("_DataB/sinhvien.txt",'r+', encoding='utf-8')
        check ="text"
        luot = 1
        while check != "":
            if luot == 2:
                ii = int(check)
                canhanList[ii].hoten = ff.readline()
                canhanList[ii].macanhan = ii
                canhanList[ii].sdt = ff.readline()
                canhanList[ii].quequan = ff.readline()
                canhanList[ii].email = ff.readline()
                giaovienList[ii].masinhvien = ff.readline()
                giaovienList[ii].ngaysinh = ff.readline()
                giaovienList[ii].gioitinh = ff.readline()
                giaovienList[ii].diachi = ff.readline()
                check = ff.readline()
            else:
                ii = int(ff.readline())
                canhanList[ii].hoten = ff.readline()
                canhanList[ii].macanhan = ii
                canhanList[ii].sdt = ff.readline()
                canhanList[ii].quequan = ff.readline()
                canhanList[ii].email = ff.readline()
                giaovienList[ii].masinhvien = ff.readline()
                giaovienList[ii].ngaysinh = ff.readline()
                giaovienList[ii].gioitinh = ff.readline()
                giaovienList[ii].diachi = ff.readline()
                check = ff.readline()
                luot = luot + 1

 ################################################################## Main ################################################
canhanList = [Canhan() for i in range (0,1000)]
sinhvienList =[Sinhvien() for i in range (0,1000)]
giaovienList = [Giaovien() for i in range (0,1000)]
khoahocList = [Khoahoc() for i in range (0,1000)]
nganhdaotaoList = [Nganhdaotao() for i in range (0,1000)]
diemList = [Diem() for i in range (0,1000)]
monhocList = [Monhoc() for i in range(0,1000)]
if __name__ == '__main__':
    tuychon = "open"
    ii = 0
    ee = open("_DataB/i.txt",'r+', encoding='utf-8')
    so = int(ee.readline())
    ee.close()
    while tuychon != "close":
        print("Bạn muốn thực hiện gì (Nhấn 0 để tắt)")
        print("1 để nhập tên sinh viên ")
        print("2 để nhập tên giáo viên ")
        print("3 để nhập tên khoá học ")
        print("4 để nhập ngành đào tạo ")
        print("5 để nhập điểm ")
        print("6 để lưu dữ liệu ")
        print("7 để tìm sinh viên ")
        print("8 để load dữ liệu")
        print("9 để add sinh viên")
        ttcheck = int(input())
        if ttcheck == 0:
            tuychon = "close"
        elif ttcheck == 1:
            ip.InputSinhvien(so)
            so = so+1
        elif ttcheck == 2:
            ip.InputGiaovien(so)
            so = so+1
        elif ttcheck == 3 :
            ip.InputKhoahoc(so)
            so = so+1
        elif ttcheck == 4:
            ip.InputNganhdaotao(so)
            so = so+1
        elif ttcheck ==5:
            print("hãy nhập mã sinh viên để nhập điểm")
            mas = int(input())
            print("nhap diem cho sinh vien ")
            print(canhanList[mas].hoten)
            ip.InputDiem(mas)
        elif ttcheck ==6:
            print("1: sinh viên \n 2: giáo viên \n 3: khoá học \n 4: ngành đào tạo \n 5: điểm ")
            ttcheck2 =int(input())
            if ttcheck2 == 1:
                for o in range(len(sinhvienList)):
                    if sinhvienList[o].masinhvien != "":
                        ip.OutputSinhvien(o)
            if ttcheck2 ==2:
                for o in range(len(giaovienList)):
                    if giaovienList[o].magiaovien != "":
                        ip.OutputGiaovien(o)
            if ttcheck2 ==3:
                ip.OutputKhoahoc(so)
            if ttcheck2 ==4: 
                ip.OutputNganhdaotao(so)
            if ttcheck2 ==5:
                for o in range(len(diemList)):
                    if diemList[o].diemtb != "":
                        ip.OutputDiem(o)
        elif ttcheck == 7:
            print("hãy nhập mã số của học sinh để tìm ")
            quanlysv.findsinhvien()
        elif ttcheck == 8:
            print("load thông tin ")
            quanlysv.docdatasv()
            quanlygv.docdatagv()
        elif ttcheck == 9:
            print("Add Sinh viên ")
            print("1 để add ngành 2 để add khoá")
            tttcheck = int(input())
            if tttcheck == 1:
                ip.AddsvNganh(so)
            else:
                ip.AddsvKhoahoc(so)
        #close while
        else:
            print("hãy nhập lại nào")
        
    ee = open("_DataB/i.txt",'w+', encoding='utf-8')
    ee.write(str(so))
    ee.close()
    

