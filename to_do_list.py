def todolist():
    daftar_tugas = []
    
    while True:
        print("="*25)
        print("To Do List sederhana")
        print("="*25)
        print("1. Menambahkan Daftar Tugas")
        print("2. Menghapus Daftar Tugas")
        print("3. Melihat Daftar Tugas")
        print("4. Keluar")
        
        pilihan = int(input("Masukan Pilihan Anda(1-4): "))
        if pilihan == 1:
            tugas = input("Masukan Tugas: ")
            daftar_tugas.append(tugas)
            print(f"Tugas {tugas} Berhasil Ditambahkan")
        elif pilihan == 2:
            tugas = input("Ketik Tugas Yang Ingin Dihapus: ")
            if tugas in daftar_tugas:
                daftar_tugas.remove(tugas)
                print(f"Tugas {tugas} Berhasil Dihapus")
                
            else:
                print("Tugas Tidak Ditemukan")
        elif pilihan == 3:
            print("Daftar Tugas: ")
            for i, tugas in enumerate(daftar_tugas, 1):
                print(f"{i} Adalah {tugas}")
        elif pilihan == 4:
            print("Keluar Dari Program ")
            break
        else:
            print("Pilihan Tidak Ada")
print("Terimakasih Sudah Menggunakan To Do List Sederhana") 
todolist()
        