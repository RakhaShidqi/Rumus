from termcolor import colored
from pyfiglet import figlet_format

print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
print(" #===========================================================================#"),'yellow'))
print(" #================ Aplikasi Penghitung luas permukaan tabung ================#"),'yellow'))
print(" #================             dan volume tabung             ================#")'yellow'))
print(" #===========================================================================#")'yellow'))
print(colored(("           Developed and maintained by RakhaShidqi                  "),'yellow'))
print("                                                                              ")

#Fungsi Untuk masukkan input jari jari dan tinggi
jari_jari = float(input("Masukkan jari jari tabung: "))
tinggi    = float(input("Masukkan tinggi tabung: "))
print("                                                                              ")

#Fungsi Untuk Membuat Rumus
luas_permukaan_tabung = (2*3.14*jari_jari*(jari_jari+tinggi))
volume_tabung         = (3.14*jari_jari**2*tinggi)

#Fungsi Untuk Mengeluarkan Outputnya
print("Luas Permukaan Tabung Adalah: ",luas_permukaan_tabung)
print("Volume Tabung Adalah: ",volume_tabung)
print("                                                                              ")
