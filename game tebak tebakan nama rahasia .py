import os

print("""
  *******************GAME TEBAK NAMA RAHASIA**********************
Daftar nama : septi, bayu, budi, tono, dika, danu, anto, elga, safi
Player 1: Buatlah nama rahasia dari daftar nama diatas! \n
""")
secret=str(input("Masukkan Nama rahasia 'player 1' : "))
os.system('cls')

print("""
===================***************************======================
Player 1 sudah membuat nama yang akan ditebak, silahkan tebak :D
===================***************************======================""")
batas=3
for percobaan in range(batas):
    jawaban=str(input(f"Masukkan tebakan player 2 : "))
    if jawaban == secret:
        print("Selamat, tebakan anda benar !!!")
        break
    else:
        print(f"Maaf jawaban , coba lagi...\n{batas-(percobaan+1)}x tebak lagi")
if percobaan == batas-1:
    print("kamu telah kalah dalam permainan ini")