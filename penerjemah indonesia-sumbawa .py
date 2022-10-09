print("*******************====TERJEMAHAN BAHASA SUMBAWA====***********************")

dict={
    'saya' : 'kaji',
    'kamu' : 'sia',
    'mandi' : 'maneng',
    'makan' : 'mangan',
    'tidur' : 'tunung'
}
terjemahan=input("Masukkan kata yang ingin di terjemahkan: ")
if terjemahan=='saya':
    print(f"Saya : {dict['saya']}")
elif terjemahan=='kamu':
    print(f"Kamu : {dict['kamu']}")
elif terjemahan=='mandi':
    print(f"Mandi : {dict['mandi']}")
elif terjemahan=='makan':
    print(f"Makan : {dict['makan']}")
elif terjemahan=='tidur':
    print(f"Tidur : {dict['tidur']}")
else:
    print("INVALID")