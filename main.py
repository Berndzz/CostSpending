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
    jumlah = float(jumlah_input.replace(".", "").replace(",", ""))

    # Tombol untuk menyimpan pengeluaran dan menampilkan tautan unduh
    if st.button("Simpan dan Tampilkan"):
        st.session_state.data = st.session_state.data.append(
            {"Tanggal": tanggal, "Deskripsi": deskripsi, "Jumlah": jumlah},
            ignore_index=True,
        )

    # Menampilkan pengeluaran yang sudah disimpan
    st.subheader("Data Pengeluaran")
    st.write(st.session_state.data)

    # Tampilkan tombol unduh
    file_name = f"pengeluaran_{tanggal.day}_{tanggal.strftime('%B')}_{tanggal.year}.txt"
    st.download_button(
        label=f"Download File {file_name}",
        data=st.session_state.data.to_csv(index=False, sep="\t"),
        file_name=file_name,
        mime="text/plain",
    )


if __name__ == "__main__":
    main()
