# StudiKasus6DDP
<img width="559" height="224" alt="image" src="https://github.com/user-attachments/assets/29151e90-3ec0-4613-b673-81b7fb64962b" />
<br>
Koneksi antara python ke file json, menggunakan library json sebagai penghubung agar file bisa berinteraksi dan os untuk mengecek dan berinteraksi dengan file json, apakah ada duplikat atau tidak, serta merubah nama file menjadi variabel untuk memudahkan koneksinya.
<br>
mengecek apakah data baru yang ingin ditambahkan sudah ada ataupun tidak menggunakan "not os.path.exists",
file menggunakan "w" yang berarti "write", lalu file di isi dengan list kosong menggunakan "json.dump"
<br>
<img width="536" height="145" alt="image" src="https://github.com/user-attachments/assets/f4778e41-84cf-4db3-9b7d-c2ce5b47dad7" />
<br>
"json.load(f)" untuk mengubah isi list menjadi dictionary, dan "try, except" untuk persiapan apabila data belum terisi ataupun file tidak ada, agar looping tidak langsung terhenti menggunakan "return[]".
<br>
<img width="444" height="87" alt="image" src="https://github.com/user-attachments/assets/e943f2a9-4783-41ea-a8fd-e14b1bab7089" />
<br>
Digunakan untuk menyimpan data ke dalam file json
<br>
<img width="721" height="271" alt="image" src="https://github.com/user-attachments/assets/3a526220-7753-4a72-8faf-4f3d16422521" />
<br>
"data = baca_data()" untuk mengubah function "baca_data()" menjadi variabel, agar mempermudah coding, lalu "if not data" apabila list tidak berisi,"print(f"{'No':<4}{'Kode':<10}{'Nama Barang':<25}{'Stok':<8}{'Harga':>12}")" dan "print("-" * 59)" sebagai nama kolom dan pemisah, (:<8, :<12) digunakan untuk mengatur jarak agar terlihat baik.
<br>
lalu perulangan for untuk menambahkan nomor secara otomatis, dimulai dari 1, dan "len(data)" yang digunakan untuk menghitung jumlah barang yang ditampilkan diakhir.
<br>
<img width="735" height="443" alt="image" src="https://github.com/user-attachments/assets/d9b42fa5-12f2-43ea-99f4-82d97e039c9d" />
<br>
menggunakan ".strip()" di input untuk membuang spasi di awal ataupun akhir, lalu pengecekan apakah data sudah sesuai kriteria menggunakan logika "or" di bagian kode dan nama, serta "and" di bagian stok dan harga, menggunakan "isdigit()" untuk memastikan bahwa yang dimasukkan berupa angka dan bukan huruf.
<br>
apabila semua kriteria sudah terpenuhi, data akan disimpan kedalam file json menggunakan "data.append".
<br>
<img width="482" height="429" alt="image" src="https://github.com/user-attachments/assets/df8b8299-c958-472a-94e4-46ebe1bca45d" />
<br>
memanggil "data_inven()" agar menu bisa berfungsi, karena tanpa itu, koneksi antara file json dan python akan terputus, lalu perulangan "while" agar program berjalan terus menerus, "if" "elif" dan "else" sebagai penentu kelanjutan program yang akan dilanjutkan berdasarkan input.
<br>
<img width="756" height="459" alt="image" src="https://github.com/user-attachments/assets/661ba02c-015c-4259-ab82-da7840126bf0" />
<br>
file json sebelum ditambahkan apa apa.
<br>
<img width="507" height="308" alt="image" src="https://github.com/user-attachments/assets/757ace11-6804-4119-8a24-56c4c2865bab" />
<br>
menambahkan isi dictionary kedalam file json.
<br>
<img width="405" height="345" alt="image" src="https://github.com/user-attachments/assets/5003a762-66a2-4158-af09-2954adced6cb" />
<br>
isi file json setelah ditambahkan isi.
<br>
<img width="485" height="281" alt="image" src="https://github.com/user-attachments/assets/e452f914-dde9-4929-a405-4e96136ceb0b" />
<br>
menggunakan fungsi melihat data untuk melihat apa yang ada di dalam file json.
