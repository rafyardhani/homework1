# Home Work 1 - Scraping Tokopedia
## Permasalahan yang dihadapi
### Variabel yang berbeda beda
Tidak semua produk memiliki struktur yang sama, beberapa fitur yang bersifat opsional seperti
- Rating
- Jumlah produk terjual
- Persentasi Diskon
- Harga sebelum diskon

Hal ini menghasilkan error dengan tidak ditemukannya beberapa tag css sehingga dengan kondisi tersebut perlu ditambahkan sebuah kondisi (if) agar dapat mengcover kedua kondisi tersebut.

### Deploy ke Streamlit
Streamlit tidak dapat membuka webdriver sehingga menghasilkan error code Status code was: 127. Permasalahan ini dipicu dikarenakan selenium tidak bisa membuka webdriver bahkan ketika menggunakan parameter headless. Selain itu, saat menggunakan function 
```
driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
```
menghasilkan error karena tidak ditemukan. Asumsi saat ini dikarenakan pada saat meng-eksekusi code tersebut perlu membuka webdriver serta tag button harus terlihat pada screen/webdriver yang dibuka.

### Waktu runtime yang cukup lama
Kondisi saat ini jika menggunakan code CSS_SELECTOR diperlukan membuka webdriver (baik itu firefox atau chrome) maka membutuhkan waktu yang cukup lama, selain itu kondisi internet juga mempengaruhi karena perlu menunggu seluruh konten dimuat. Kondisi ini dipengaruhi oleh jumlah limitasi page yang ditentukan ketika menjalankan program scraping dan kondisi internet yang tersedia.

### Thumbnail
Permasalahan yang jarang terjadi tetapi cukup mengganggu karena dapat membuat runtime menjadi error dikarenakan tidak terdapat gambar produk. Beberapa produk memiliki thumbnail dengan tipe video, ketika selenium berjalan dan cursor mengarah kepada produk yang memiliki thumbnail video maka error karena tag yang berbeda dengan thumbnail lainnya.

### Menjalankan program
melakukan clone repository 
```
git clone https://github.com/rafyardhani/homework1.git
```
Program ini menggunakan beberapa library yang dapat diinstall melalui
```
pip install -r requirements.txt
```
Setelah requirement terpasang program dapat dijalankan dengan menggunakan perintah berikut.
```
streamlit run main2.py
```