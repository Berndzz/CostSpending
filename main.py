import streamlit as st
from datetime import datetime


def main():
    st.title("Aplikasi Pencatatan Pengeluaran Harian")

    # Tampilkan form untuk input pengeluaran
    st.subheader("Input Pengeluaran")
    tanggal = st.date_input("Tanggal", datetime.today())
    deskripsi = st.text_input("Deskripsi")
    # Menggunakan widget text_input untuk memasukkan jumlah dalam format uang Rupiah
    jumlah_input = st.text_input("Jumlah (dalam ribuan)", value="0")
    jumlah = int(jumlah_input.replace(".", ""))

    # Tombol untuk menyimpan pengeluaran dan menampilkan tautan unduh
    if st.button("Simpan dan Unduh"):
        file_name = (
            f"pengeluaran_{tanggal.day}_{tanggal.strftime('%B')}_{tanggal.year}.txt"
        )

        with open(file_name, "a") as file:
            file.write(f"Tanggal\tDeskripsi\tJumlah\n")
            file.write(f"{tanggal}\t{deskripsi}\t{jumlah}\n")

        st.success(f"Data berhasil disimpan ke dalam file {file_name}.")

        # Hitung total pengeluaran
        total_pengeluaran = jumlah

        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.split("\t")
                total_pengeluaran += int(parts[2])

        with open(file_name, "a") as file:
            file.write("--------------------------------+\n")
            file.write(f"Total Pengeluaran:\t{total_pengeluaran}\n")

        # Tampilkan tombol unduh
        st.download_button(
            label=f"Download File {file_name}",
            data=open(file_name, "rb"),
            file_name=file_name,
            mime="text/plain",
        )

    # Menampilkan pengeluaran yang sudah disimpan
    st.subheader("Data Pengeluaran")
    st.write("Tanggal\tDeskripsi\tJumlah\n")
    st.write("---\t---\t---")

    # Menampilkan total pengeluaran
    total_pengeluaran = 0

    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            parts = line.split("\t")
            st.write(f"{parts[0]}\t{parts[1]}\t{parts[2]}")
            total_pengeluaran += int(parts[2])

    st.write("--------------------------------+\n")
    st.write(f"Total Pengeluaran:\t{total_pengeluaran}")


if __name__ == "__main__":
    main()
