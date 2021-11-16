#########################################################################################################
#------------------------------------------BACK-END-----------------------------------------------------#
#########################################################################################################


import time
from typing import List
input("masukkan data")

#CARI DATA#
def backend_cari():

    #integrating
    dapatentrynamacari = entrynamacari.get()

    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "r")
    listdata = file.readlines()
    data_nama = listdata[0]
    baru_nama = data_nama.split(',')
    tampungnama = dapatentrynamacari #integrad
    tampungnamabesar = tampungnama.upper()
    caridata = baru_nama.index(tampungnamabesar)
    memasukkan = caridata
    file.close()

    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "r")
    listdata = file.readlines()
    list_nama = listdata[0]
    baru_nama = list_nama.split(',')
    memunculkannamacari = (f"nama : {baru_nama[memasukkan]}")
    file.close()

    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_NIK.txt", "r")
    listdata = file.readlines()
    list_NIK = listdata[0]
    baru_NIK = list_NIK.split(',')
    memunculkanNIKcari = (f"NIK  : {baru_NIK[memasukkan]}")
    file.close()

    #buka jendela baru
    windowbarucari= Toplevel(WINDOW)
    windowbarucari.geometry("500x250")
    windowbarucari.title("Hasil Pencarian")

    hasilnamacari = Label(windowbarucari, text= f"Nama : {baru_nama[memasukkan]}")
    hasilNIKcari = Label(windowbarucari, text= f"NIK     : {baru_NIK[memasukkan]}")

    Font_tuplemainmenu = ("Perpetua titiling MT", 14, "bold")
    hasilnamacari.configure(font = Font_tuplemainmenu, bg='white' )
    hasilNIKcari.configure(font = Font_tuplemainmenu, bg='white')

    hasilnamacari.place(relx = 0.25, rely = 0.43, anchor ='sw')
    hasilNIKcari.place(relx = 0.25, rely = 0.53, anchor ='sw')

    windowbarucari.configure(bg='white')

#LIHAT SEMUA DATA#
def popuplihatsemua():
        
    #mengambil membaca dari data nama, ambil catatan lain saja agar mudah bosqu..
    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "r")
    listdata = file.readlines()
    data_nama = listdata[0]
    baru_nama = data_nama.split(',')
    mengurut = sorted(baru_nama)
    jumlahdata = len(mengurut) - 2 #kasih angaka minus dua karena untuk mengihlangkan awalan. ini adalah menampilakn jumlah data
    file.close()

    #perulangan untuk penomoran
    for i in range(jumlahdata) : #TypeError: can only concatenate str (not "int") to str
        perulangannomor = (f' {i}') 

#ini pr nya bagaimana agar melidi kebawah nomornya

    #perulangan untuk membuat baris baru untuk nama
    for ganjil in range(2, jumlahdata + jumlahdata, 2) : #menambahkan enter pada setiap akhir nama, dengan perulangan metode lompat2
        mengurut.insert(ganjil, '\n')
    barulagi_nama = ''.join(mengurut) #menggabungkan data di list tanpa tanda khusu tambahan -> "    "

    #buat jendela
    windowbarulihatsemua = Toplevel(WINDOW)
    windowbarulihatsemua.geometry("300x750")
    windowbarulihatsemua.title(f"overview data [{jumlahdata}]")

    #atur posisi
    tampungisi = Label(windowbarulihatsemua, text=barulagi_nama, justify="left")
    tampungisi.place(relx=0.4, rely=0.03, anchor="center")
    tampungnomor = Label(windowbarulihatsemua, text=perulangannomor, justify="center")
    tampungnomor.place(relx=0.08, rely=0.03, anchor="center")

#INPUT DATA#
def backend_input():

    #integrating
    dapatentrynama = entrynama.get()
    dapatentryNIK =  entryNIK.get()
    
    nama  = dapatentrynama #menginput
    nama_besar = nama.upper()

    #input data nama
    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "a")
    file.write(f"{nama_besar},")
    file.close()

    #input data NIK
    NIK   = dapatentryNIK #menginput
    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_NIK.txt", "a")
    file.write(f"{NIK},")
    file.close()

#HAPUS DATA#
def backend_hapus():
    #integrating
    dapatentrynamahapus = entrynamahapus.get()

    #kontrol pencarian
    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "r")
    listdata = file.readlines()
    data_nama = listdata[0]
    baru_nama = data_nama.split(',')
    tampungnama = dapatentrynamahapus #menginput
    tampungnamabesar = tampungnama.upper()
    caridata = baru_nama.index(tampungnamabesar)
    file.close()

    #menghapus suatu kalimat di data
    baru_nama.pop(caridata)
    lagimemasukkan = (",".join(baru_nama))

    #mengambil data nama baru untuk di inputkan lagi
    file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "w")
    file.write(lagimemasukkan)
    file.close()

#HAPUS SEMUA DATA#
def popuphapussemua():
    windowbaruhapussemuadata= Toplevel(WINDOW)
    windowbaruhapussemuadata.geometry("250x200")
    windowbaruhapussemuadata.title('konfirmasi')
    
    def konfirmasihapusemuanama():
        file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "w")
        file.write(" ,")
        file.close()
    
    def konfirmasihapusemuaNIK():
        file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_NIK.txt", "w")
        file.write(" ,")
        file.close()

    variabelkonfirmasihapussemua = Button(windowbaruhapussemuadata, text =' Hapus Semua Data ', font='10' ,bg=birupekat, fg='white', relief='flat', activebackground=birupekat, activeforeground='white', command=lambda:[konfirmasihapusemuanama(), konfirmasihapusemuaNIK()])
    variabelkonfirmasihapussemua.place(relx = 0.5, rely = 0.47, anchor = 'center')

    #menimpa file yang sudah tersimpan dengan file kosongan
    

#########################################################################################################
#------------------------------------------FRONT-END----------------------------------------------------#
#########################################################################################################


from tkinter import *
from tkinter import font
import tkinter
from tkinter.font import Font, families
from typing import Sized, overload
from tkinter import messagebox

WINDOW = Tk()
WINDOW.geometry('780x400')
WINDOW.title('Data warga')

#warna
birupekat = '#050612'
birutengah = '#111438'
birumuda = '#1f2782'
biruputih = '#3944bf'

#animasi hover main menu
def animasihover(button, colorOnHover, colorOnLeave):

    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

#animasi main menu 
def ubahcarilabel(): 
    carilabel['bg'] = birutengah
    aktif = True
    if  aktif == True :
        inputlabel['bg'] = birumuda
        hapuslabel['bg'] = birumuda

        #memunculkan lokasi menu cari
        textnamacari.place(relx = 0.16, rely = 0.5, anchor = 'center')
        entrynamacari.place(relx = 0.5, rely = 0.5, anchor = 'center', width=390, height=30)
        submitnamacari.place(relx = 0.74, rely = 0.5, anchor = 'center')
        submitlihatsemua.place(relx = 0.845, rely = 0.5, anchor = 'center')

        animasihover(carilabel, birutengah, birutengah)
        animasihover(inputlabel, biruputih, birumuda)
        animasihover(hapuslabel, biruputih, birumuda)

def ubahinputlabel(): 
    inputlabel['bg'] = birutengah
    aktifinput = True
    if  aktifinput == True :
        carilabel['bg'] = birumuda
        hapuslabel['bg'] = birumuda

        #memunculkan lokasi menu input
        textnamainput.place(relx = 0.16, rely = 0.45, anchor = 'center')
        textNIKinput.place(relx = 0.15, rely = 0.6, anchor = 'center')
        entrynama.place(relx = 0.5, rely = 0.45, anchor = 'center', width=390, height=30)
        entryNIK.place(relx = 0.5, rely = 0.6, anchor = 'center', width=390, height=30)
        submitinputdata.place(relx = 0.5, rely = 0.75, anchor = 'center')


        animasihover(carilabel, biruputih, birumuda)
        animasihover(inputlabel, birutengah, birutengah)
        animasihover(hapuslabel, biruputih, birumuda)

def ubahhapuslabel(): 
    hapuslabel['bg'] = birutengah
    aktif = True
    if  aktif == True :
        carilabel['bg'] = birumuda
        inputlabel['bg'] = birumuda

        #memunculkan lokasi menu hapus
        textnamahapus.place(relx = 0.16, rely = 0.5, anchor = 'center')
        entrynamahapus.place(relx = 0.5, rely = 0.5, anchor = 'center', width=390, height=30)
        submitnamahapus.place(relx = 0.74, rely = 0.5, anchor = 'center')
        hapussemuadata.place(relx = 0.89, rely = 0.5, anchor = 'center')

        animasihover(carilabel, biruputih, birumuda)
        animasihover(inputlabel, biruputih, birumuda)
        animasihover(hapuslabel, birutengah, birutengah)

#mengalihkan tampilan menu
def munculmenucari():

    #memindah menu input agar tidak terlihat
    textnamainput.place(relx = 0.16, rely = 5, anchor = 'center')
    textNIKinput.place(relx = 0.15, rely = 5, anchor = 'center')
    entrynama.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    entryNIK.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    submitinputdata.place(relx = 0.74, rely = 5, anchor = 'center')

    
    #memindah menu hapus agar tidak terlihat
    textnamahapus.place(relx = 0.16, rely = 5, anchor = 'center')
    entrynamahapus.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    submitnamahapus.place(relx = 0.74, rely = 5, anchor = 'center')
    hapussemuadata.place(relx = 0.74, rely = 5, anchor = 'center')


    #memindah kata pembuka
    katapembuka.place(relx = 0.5, rely = 5, anchor = 'center')
    katapembukakecil.place(relx = 0.5, rely = 5, anchor = 'center')

def munculmenuinput():
    #memindah menu cari agar tidak terlihat
    textnamacari.place(relx = 0.16, rely = 5, anchor = 'center')
    entrynamacari.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    submitnamacari.place(relx = 0.74, rely = 5, anchor = 'center')
    submitlihatsemua.place(relx = 0.853, rely = 5, anchor = 'center')
    hapussemuadata.place(relx = 0.74, rely = 5, anchor = 'center')

    #memindah menu hapus agar tidak terlihat
    textnamahapus.place(relx = 0.16, rely = 5, anchor = 'center')
    entrynamahapus.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    submitnamahapus.place(relx = 0.74, rely = 5, anchor = 'center')

    #memindah kata pembuka
    katapembuka.place(relx = 0.5, rely = 5, anchor = 'center')
    katapembukakecil.place(relx = 0.5, rely = 5, anchor = 'center')

def munculmenuhapus():
    #memindah menu cari agar tidak terlihat
    textnamacari.place(relx = 0.16, rely = 5, anchor = 'center')
    entrynamacari.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    submitnamacari.place(relx = 0.74, rely = 5, anchor = 'center')
    submitlihatsemua.place(relx = 0.853, rely = 5, anchor = 'center')

    #memindah menu input agar tidak terlihat
    textnamainput.place(relx = 0.16, rely = 5, anchor = 'center')
    textNIKinput.place(relx = 0.15, rely = 5, anchor = 'center')
    entrynama.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    entryNIK.place(relx = 0.5, rely = 5, anchor = 'center', width=390, height=30)
    submitinputdata.place(relx = 0.74, rely = 5, anchor = 'center')


    #memindah kata pembuka
    katapembuka.place(relx = 0.5, rely = 5, anchor = 'center')
    katapembukakecil.place(relx = 0.5, rely = 5, anchor = 'center')

#kata pembuka
katapembuka = Label(WINDOW, text= "Selamat Datang Kembali", bg=birutengah, fg='white')
katapembukakecil = Label(WINDOW, text= "silahkan pilih menu diatas", bg=birutengah, fg='white')

#set lokasi kata pembuka
katapembuka.place(relx = 0.5, rely = 0.43, anchor = 'center')
katapembukakecil.place(relx = 0.5, rely = 0.6, anchor = 'center')

#main menu
carilabel = Button(WINDOW, text='                     CARI                  ', relief=FLAT, bg=birumuda, fg='white', activebackground=birutengah, activeforeground='white', command=lambda:[ubahcarilabel(), munculmenucari()]) #ini adalah menggunakan 2 function(def) dalam 1 command
inputlabel = Button(WINDOW, text='                 INPUT                   ', relief=FLAT, bg=birumuda, fg='white', activebackground=birutengah, activeforeground='white',command=lambda : [ubahinputlabel(), munculmenuinput()]) #jika ingin menggunakan 1 function saja, juga bisa ...
hapuslabel = Button(WINDOW, text='                 HAPUS                    ', relief=FLAT, bg=birumuda, fg='white', activebackground=birutengah, activeforeground='white', command=lambda :[ubahhapuslabel(), munculmenuhapus()]) #dengan menuliskan command=ubahhapuslabel

#animasi main menu saat pertama
animasihover(carilabel, biruputih, birumuda)
animasihover(inputlabel, biruputih, birumuda)
animasihover(hapuslabel, biruputih, birumuda)

#set location main menu
carilabel.grid(column=1, row=0)
inputlabel.grid(column=2, row=0)
hapuslabel.grid(column=3, row=0)

#menu CARI 
textnamacari = Label(WINDOW, text ='Nama' ,bg=birutengah, fg='white')
entrynamacari = Entry(WINDOW, relief ="groove", width=50)
submitnamacari = Button(WINDOW, text =' cari ', font='10' ,bg=birupekat, fg='white', relief='flat', activebackground=birupekat, activeforeground='white', command=backend_cari)

#submenu lihat semua
#mendapatkan jumlah data
file = open("D:\dokumen\Academic\Pemograman\python\proyek python\Tulis Baca Simpan Data\data_nama.txt", "r")
listdata = file.readlines()
data_nama = listdata[0]
baru_nama = data_nama.split(',')
jumlahdata = len(baru_nama)
file.close()

submitlihatsemua = Button(WINDOW, text =f' lihat semua', font='10' ,bg=birupekat, fg='white', relief='flat', activebackground=birupekat, activeforeground='white', command=popuplihatsemua)


#menu INPUT
textnamainput = Label(WINDOW, text ='Nama' ,bg=birutengah, fg='white')
textNIKinput = Label(WINDOW, text ='NIK', font='10' ,bg=birutengah, fg='white')
entrynama = Entry(WINDOW, relief ="groove", width=50)
entryNIK = Entry(WINDOW, relief ="groove", width=50)

submitinputdata = Button(WINDOW, text =' submit ', font='10' ,bg=birupekat, fg='white', relief='flat', activebackground=birupekat, activeforeground='white', command=backend_input)


#menu HAPUS
textnamahapus = Label(WINDOW, text ='Nama' ,bg=birutengah, fg='white')
entrynamahapus = Entry(WINDOW, relief ="groove", width=50)
submitnamahapus = Button(WINDOW, text =' hapus ', font='10' ,bg=birupekat, fg='white', relief='flat', activebackground=birupekat, activeforeground='white', command=backend_hapus)
hapussemuadata = Button(WINDOW, text =' hapus semua data ', font='10' ,bg=birupekat, fg='white', relief='flat', activebackground=birupekat, activeforeground='white', command=popuphapussemua)

#configure katapembuka
Font_tuplekatapembuka = ("Perpetua titiling MT", 42, "bold")
katapembuka.configure(font = Font_tuplekatapembuka)
katapembukakecil.configure(font = ("Perpetua titiling MT", 19))

#configure main menu
Font_tuplemainmenu = ("Perpetua titiling MT", 14, "bold")
carilabel.configure(font = Font_tuplemainmenu )
inputlabel.configure(font = Font_tuplemainmenu)
hapuslabel.configure(font = Font_tuplemainmenu)

#configure menu
textnamainput.configure(font= ("", 12, "bold"))
textNIKinput.configure(font= ("", 12, "bold"))
entrynama.configure(font= ("", 12, "bold"))
entryNIK.configure(font= ("", 12, "bold"))

textnamahapus.configure(font= ("", 12, "bold"))
entrynamahapus.configure(font= ("", 12, "bold"))
hapussemuadata.configure(font= ("", 12))

textnamacari.configure(font= ("", 12, "bold"))
entrynamacari.configure(font= ("", 12, "bold"))
submitlihatsemua.configure(font= ("", 12))

#copyright
pojoktulisan = Label(WINDOW, text ='Made by Sigit khoirul anam', bg=birutengah, fg='white')
pojoktulisan.place(relx = 0.0, rely = 1.0, anchor ='sw')


#disable rezise window
WINDOW.resizable(False, False)
WINDOW.configure(bg=birutengah)
WINDOW.mainloop()

#note
#apabila variabel adalah tk.Tk() maka jika gunakan juga .tk ketika ingin memanggil
#sedangkan jika hanya Tk() maka tidak pelu menuliskan tk.XXXX tetapi langsung saja
#metode memilih tempat untuk menjalankan CMD, yaitu dengan memilih lokasi direktori, kemudian dipeta direktori silahkan ketik CMD
