import qrcode
from PIL import Image
import streamlit as st
import io

# Predefined color pairs as a dictionary
color_pairs = {
    "Black on White": ("#000000", "#FFFFFF"),
    "Black on Yellow": ("#000000", "#FFFFAA")
}

def generate_qr_code(url, fill_color, bg_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)
    return img

# st.header("E-Ticket Registration")
st.markdown('## E-Ticket :orange[Registration]')
st.divider()
st.markdown('#### เฉพาะท่านมี :orange[หมายเลขบัตร] เท่าน้ัน')
st.markdown('- :red[ชื่อ, นามสกุล,] ต้อง :red[เว้นวรรค] หลังชื่อ, ไม่มีคำนำหน้า :red[นาย / นาง]')
st.markdown('- :red[สังกัด] ภาค, หน่วย, (ต้องใส่ :red[-] :gray[ระหว่างเลข])')
st.markdown('- :red[โทร.] ต้องมีขีด - ระหว่างเลข :red[000-000-0000]')
st.markdown('- :red[หมายเลขบัตร] ต้องใส่ -- :red[#] --นำหน้า')

# Get the URL input from the user
url = st.text_input("QR Code Generator")

# Allow the user to choose a color pair
color_pair = st.selectbox("เลือกสี", list(color_pairs.keys()))

# Add a button to generate the QR code and download it
if st.button("สร้าง QR Code") and url:
    try:
        fill_color, bg_color = color_pairs[color_pair]
        qr_img = generate_qr_code(url, fill_color, bg_color)
        
        # Save the PIL Image to a BytesIO buffer and convert it to bytes
        img_buffer = io.BytesIO()
        qr_img.save(img_buffer, format="PNG")
        img_bytes = img_buffer.getvalue()
        
        # Add a download button
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            key="qr_code_download",
            file_name="qr_code.png",
            mime="image/png",
        )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


st.divider()

md = st.text_area('ให้กดปุ่ม :red[ดาวน์โหลด]',
                  'ให้บันทึกและเก็บติดตัวเป็น E-Ticket เพื่อนำไปสแกนที่หน้างาน '
                  ) 
