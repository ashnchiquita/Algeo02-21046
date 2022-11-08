import configImages as ci
import function as fc
import cv2

# ini kukasih print biar tau aja udah sampe mana soalnya runningny lama

# TRAINING

# Menyiapkan data, membuat himpunan matriks training image (Run 5000 taun)
# matList : list of mat
pathfolder = "Algeo02-21046/test"
          
matList = ci.readFolderImages(pathfolder)

print("Berhasil mengekstraksi training image!")

# Mencari mean dari matList
# mean : mat
mean = fc.mean(matList)

print("Berhasil menghitung mean training image! Klik esc setelah gambar muncul!")

cv2.imshow("mean",mean/255)
cv2.waitKey()
cv2.imwrite("Algeo02-21046/src/mean.jpg", mean)

# Membuat himpunan matriks selisih
# selisihList : list of mat
selisihList = []
for mat in matList:
    selisihList.append(fc.selisihMeanMat(mat, mean))
    
print("Berhasil menghitung selisih matriks training image dan mean!")
    
# Menghitung matriks kovarian
# kov : mat
kov = fc.covarian(selisihList)

# # UNCOMMENT KALO UDAH BENER (cmd + K + U atau apapun di windowsny)
# # Menghitung eigenvalue
# # eigenVal : list of float
# eigenVal = fc.eigenval(kov)

# # Menghitung eigenvector
# # eigenVecs : list of vector / list of mat
# # eigenVecs = fc.eigenvec(selisihList, eigenVal)

# # Menghitung eigenface
# # eigenfaceList = []
# # for eigenVec in eigenVecs:
# #     eigenfaceList.append(fc.eigenfaceMat(selisihList, eigenVec))

# # TAHAP PENGENALAN WAJAH
# # Insert Test Face
# # ini simulasi aja, nanti kan pake GUI jadi udah jelas tombolnya yang mana aja
# print("Pilih metode masukan image: \n1. Melalui upload foto\n2. Melalui webcam")
# pilihan = int(input("Masukkan pilihan : "))
# while (pilihan != 1 or pilihan != 2):
#     print("Masukan tidak valid. Silakan ulangi.")
#     pilihan = int(input("Masukkan pilihan : "))

# if (pilihan == 1):
#     # sementara asumsi <upload foto> -> masukin nama file
#     testImgPath = input("Masukkan path image test : ")
#     testFace = ci.readImage(testImgPath)
# else: # pilihan == 2
#     testFace = ci.convertFrame(ci.takePhoto())
    
# # Hitung eigenface testing image
# # eigenfaceNew = fc.eigenfaceNew()