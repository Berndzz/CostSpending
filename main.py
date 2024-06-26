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
    jumlah = jumlah_input.replace(".", "").replace(",", "")

    # Tombol untuk menyimpan pengeluaran dan menampilkan tautan unduh
    if st.button("Simpan dan Tampilkan"):
        st.session_state.data = st.session_state.data.append(
            {"Tanggal": tanggal, "Deskripsi": deskripsi, "Jumlah": jumlah},
            ignore_index=True,
        )

    # Menampilkan pengeluaran yg sudah disimpan
    st.subheader("Data Pengeluaran")
    st.write(st.session_state.data)

    # Tampilkan total pengeluaran
    total_pengeluaran = sum(st.session_state.data["Jumlah"].astype(int))
    st.subheader("Total Pengeluaran")
    st.write(f"Total Pengeluaran: Rp {total_pengeluaran:,.2f}")

    # Tampilkan tombol unduh
    file_name = f"pengeluaran_{tanggal.day}_{tanggal.strftime('%B')}_{tanggal.year}.txt"
    file_content = (
        st.session_state.data.to_csv(index=False, sep="\t")
        + f"\nTotal Pengeluaran: Rp {total_pengeluaran:,.2f}"
    )
    st.download_button(
        label=f"Download File {file_name}",
        data=file_content,
        file_name=file_name,
        mime="text/plain",
    )


if __name__ == "__main__":
    main()
