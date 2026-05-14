import streamlit as st
from fpdf import FPDF

# إعداد الصفحة
st.set_page_config(page_title="نظام تقارير الأمن", layout="centered")

class PDF(FPDF):
    def header(self):
        # إضافة شعار عماد على اليسار وشعار جند على اليمين
        # تأكد أن الأسماء مطابقة تماماً لما هو مرفوع في GitHub
        try:
            self.image('amaad_logo.png', 10, 8, 33)
            self.image('jond_logo.png', 170, 8, 33)
        except:
            pass
        
        self.set_font('Arial', 'B', 15)
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# واجهة التطبيق
st.title("نموذج تقرير أمني")

col1, col2 = st.columns(2)

with col1:
    date = st.date_input("التاريخ")
    # التعديل اللي طلبته لخانة الوقت
    time = st.text_input("الوقت (مثال: 13:15)")

with col2:
    location = st.text_input("الموقع (مثال: P4T4)")
    officer_name = st.text_input("اسم المناوب")

incident_details = st.text_area("تفاصيل الملاحظة / الإجراء المتخذ")

if st.button("تحميل التقرير PDF"):
    pdf = PDF()
    pdf.add_page()
    
    # تنبيه: الـ FPDF الأساسية لا تدعم العربي مباشرة بدون مكتبة إضافية
    # لكن هذا الترتيب يضمن عمل الكود برمجياً
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Time: {time}", ln=True)
    pdf.cell(200, 10, txt=f"Location: {location}", ln=True)
    pdf.cell(200, 10, txt=f"Officer: {officer_name}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Details: {incident_details}")
    
    pdf_output = pdf.output(dest='S').encode('latin-1', errors='replace')
    
    st.download_button(
        label="اضغط هنا لتحميل الملف",
        data=pdf_output,
        file_name=f"report_{date}.pdf",
        mime="application/pdf"
    )
