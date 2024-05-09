import streamlit as st
import pandas as pd
from datetime import datetime


def main():
    st.title("Aplikasi Pencatatan Pengeluaran Harian")

    # Membuat dataframe kosong untuk menyimpan data pengeluaran
    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=["Tanggal", "Deskripsi", "Jumlah"])

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
        st.session_state.data = st.session_state.data.append(
            {"Tanggal": tanggal, "Deskripsi": deskripsi, "Jumlah": jumlah},
            ignore_index=True,
        )

        # Menetapkan format untuk kolom Jumlah
        st.session_state.data["Jumlah"] = st.session_state.data["Jumlah"].map(
            "Rp{:,.2f}".format
        )

        # Menyimpan dataframe ke file CSV
        st.session_state.data.to_csv(file_name, index=False, sep="\t")

        st.success(f"Data berhasil disimpan ke dalam file {file_name}.")

        # Tambahkan total pengeluaran di akhir file
        total_pengeluaran = st.session_state.data["Jumlah"].sum()
        with open(file_name, "a") as file:
            file.write("\n--------------------------------+\n")
            file.write(f"Total Pengeluaran: Rp{total_pengeluaran:,.2f}\n")

        # Tampilkan tombol unduh
        st.download_button(
            label=f"Download File {file_name}",
            data=open(file_name, "rb"),
            file_name=file_name,
            mime="text/plain",
        )

    # Menampilkan pengeluaran yang sudah disimpan
    st.subheader("Data Pengeluaran")
    st.write(st.session_state.data)

    # Menampilkan total pengeluaran
    total_pengeluaran = st.session_state.data["Jumlah"].sum()
    st.subheader("Total Pengeluaran")
    st.write(f"Rp{total_pengeluaran:,.2f}")


if __name__ == "__main__":
    main()
