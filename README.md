# Tutorial: Membuat Todo List Django Clean Architecture

Berikut langkah-langkah pembuatan project Todo List ini:

## 1. Inisialisasi Project & App
1. Install Django (`pip install django`).
2. Inisialisasi project: `django-admin startproject todolist .`
3. Buat app utama: `python manage.py startapp app`

## 2. Struktur Folder
1. Buat folder `templates/`, dan `static/` di dalam app.

## 3. Model
1. Definisikan model `Todo` di `app/models.py` dengan field: `title`, `completed`, `created_at`, `updated_at`.

## 4. Admin
1. Daftarkan model Todo di `app/admin.py` agar bisa dikelola lewat admin.

## 5. Migrasi Database
1. Jalankan `python manage.py makemigrations` dan `python manage.py migrate`.

## 6. Form
1. Buat `app/forms.py` dengan `TodoForm` (ModelForm) untuk input todo.

## 7. Views
1. Buat view `todo_list` untuk menampilkan dan menambah todo.
2. Tambahkan view `todo_update`, `todo_delete`, dan `todo_toggle` untuk fitur edit, hapus, dan centang selesai.

## 8. URL
1. Atur `app/urls.py` untuk routing ke semua fitur.
2. Include `app.urls` di `todolist/urls.py`.

## 9. Template
1. Buat `app/templates/todo_list.html` dengan:
  - Form tambah/edit todo
  - Daftar todo dengan tombol edit, hapus, dan toggle selesai
  - Gunakan `{% load static %}` dan import CSS

## 10. Static Files
1. Buat `app/static/todo.css` untuk desain modern dan responsif.

## 11. Jalankan Server
1. `python manage.py runserver` lalu akses http://127.0.0.1:8000/
