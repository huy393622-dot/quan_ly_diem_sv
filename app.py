import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cài đặt giao diện trang
st.set_page_config(page_title="Quản lý Điểm Sinh Viên", layout="wide")

# Hiển thị tiêu đề[cite: 2]
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# --- XỬ LÝ DỮ LIỆU ---
# Tạo DataFrame và tính toán giống như trong Colab
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [9.0, 8.0, 7.0, 10.0, 8.0, 6.0, 9.0, 8.0, 7.0, 10.0],
    'Giữa kỳ': [8.0, 9.0, 6.0, 9.0, 7.0, 5.0, 8.0, 7.0, 8.0, 9.0],
    'Cuối kỳ': [7.5, 8.5, 6.5, 9.5, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0]
}
df = pd.DataFrame(data)

df['Tổng kết'] = 0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# --- HIỂN THỊ LÊN WEB APP ---

# 1. Hiển thị bảng điểm[cite: 2]
st.subheader("1. Bảng điểm danh sách sinh viên")
st.dataframe(df)

# 2. Hiển thị các thống kê[cite: 2]
st.subheader("2. Thống kê chung")
diem_tb = df['Tổng kết'].mean()
max_score = df['Tổng kết'].max()
min_score = df['Tổng kết'].min()
sv_cao_nhat = df[df['Tổng kết'] == max_score]['Họ và tên'].tolist()
sv_thap_nhat = df[df['Tổng kết'] == min_score]['Họ và tên'].tolist()
so_sv_dat = len(df[df['Tổng kết'] >= 5.0])

col1, col2 = st.columns(2)
with col1:
    st.info(f"**Điểm trung bình của lớp:** {diem_tb:.2f}")
    st.success(f"**Số sinh viên đạt:** {so_sv_dat}/10")
with col2:
    st.warning(f"**Sinh viên điểm cao nhất:** {', '.join(sv_cao_nhat)} ({max_score:.2f} điểm)")
    st.error(f"**Sinh viên điểm thấp nhất:** {', '.join(sv_thap_nhat)} ({min_score:.2f} điểm)")

# 3. Tra cứu sinh viên bằng Selectbox[cite: 2]
st.subheader("3. Tra cứu điểm sinh viên")
danh_sach_sv = df['Họ và tên'].tolist()
# Tạo Selectbox
sinh_vien_chon = st.selectbox("Chọn sinh viên để xem chi tiết điểm:", danh_sach_sv)

# Khi chọn sinh viên, hiển thị thông tin[cite: 2]
if sinh_vien_chon:
    thong_tin = df[df['Họ và tên'] == sinh_vien_chon].iloc[0]
    st.write(f"### Kết quả học tập của sinh viên: **{thong_tin['Họ và tên']}**")
    st.write(f"- **Điểm chuyên cần:** {thong_tin['Chuyên cần']}")
    st.write(f"- **Điểm giữa kỳ:** {thong_tin['Giữa kỳ']}")
    st.write(f"- **Điểm cuối kỳ:** {thong_tin['Cuối kỳ']}")
    st.write(f"- **Điểm TỔNG KẾT:** {thong_tin['Tổng kết']:.2f}")
    st.write(f"- **XẾP LOẠI:** {thong_tin['Xếp loại']}")

# 4. Hiển thị biểu đồ cột[cite: 2]
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Họ và tên'], df['Tổng kết'], color='cornflowerblue')
ax.set_xlabel('Điểm')
ax.set_ylabel('Tên sinh viên')
ax.set_title('Điểm tổng kết của sinh viên')
ax.set_xlim(0, 10)
ax.invert_yaxis()
st.pyplot(fig)

# 5. Thông tin người tạo (Kích thước chữ nhỏ ở cuối trang)[cite: 2]
st.markdown("---")
# LƯU Ý: Em nhớ sửa lại Tên và Mã Số Sinh Viên của em ở dòng dưới nhé!
st.markdown("<p style='text-align: center; font-size: 12px;'>Người tạo: [Nhập Họ tên của em] - MSSV: [Nhập MSSV của em]</p>", unsafe_allow_html=True)