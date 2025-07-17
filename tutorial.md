# Tutorial: Membuat Todo List Django Clean Architecture

Berikut langkah-langkah pembuatan project Todo List ini:

## 1. Inisialisasi Project & App
1. Buat virtual environment dan aktifkan.
2. Install Django (`pip install django`).
3. Inisialisasi project: `django-admin startproject todolist .`
4. Buat app utama: `python manage.py startapp app`

## 2. Struktur Folder
- Buat folder `templates/`, dan `static/` di dalam app.

## 3. Model
- Definisikan model `Todo` di `app/models.py` dengan field: `title`, `completed`, `created_at`, `updated_at`.

## 4. Admin
- Daftarkan model Todo di `app/admin.py` agar bisa dikelola lewat admin.

## 5. Migrasi Database
- Jalankan `python manage.py makemigrations` dan `python manage.py migrate`.

## 6. Form
- Buat `app/forms.py` dengan `TodoForm` (ModelForm) untuk input todo.

## 7. Views
- Buat view `todo_list` untuk menampilkan dan menambah todo.
- Tambahkan view `todo_update`, `todo_delete`, dan `todo_toggle` untuk fitur edit, hapus, dan centang selesai.

## 8. URL
- Atur `app/urls.py` untuk routing ke semua fitur.
- Include `app.urls` di `todolist/urls.py`.

## 9. Template
- Buat `app/templates/todo_list.html` dengan:
  - Form tambah/edit todo
  - Daftar todo dengan tombol edit, hapus, dan toggle selesai
  - Gunakan `{% load static %}` dan import CSS

## 10. Static Files
- Buat `app/static/todo.css` untuk desain modern dan responsif.

## 11. Jalankan Server
- `python manage.py runserver` lalu akses http://127.0.0.1:8000/

## 12. (Opsional) Admin
- Buat superuser: `python manage.py createsuperuser` untuk input data via admin.

---

**Catatan:**
- Semua logic utama diletakkan di views dan forms, bisa dipindah ke `services/` untuk arsitektur lebih bersih.
- Untuk pengembangan lebih lanjut, tambahkan validasi, notifikasi, atau fitur CRUD lanjutan sesuai kebutuhan.
