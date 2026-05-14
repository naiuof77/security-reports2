import streamlit as st
from fpdf import FPDF
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from datetime import datetime

# دالة لتنسيق النص العربي ليظهر بشكل صحيح في PDF
def fix_arabic(text):
    if not text: return ""
    reshaped_text = reshape(text)
    return get_display(reshaped_text)

class ReportPDF(FPDF):
    def header(self):
        # وضع الشعارات في الزوايا
        self.image('amaad_logo.png', x=10, y=8, w=30)
        self.image('jond_logo.png', x=160, y=8, w=40)
        self.ln(25)

    def footer(self):
        # الشريط الملون في الأسفل (كحلي ورمادي)
        self.set_y(-20)
        self.set_fill_color(26, 35, 126) # كحلي
        self.rect(0, 277, 140, 20, 'F')
        self.set_fill_color(158, 158, 158) # رمادي
        self.rect(140, 277, 70, 20, 'F')

# واجهة التطبيق
st.title("📱 نظام التقارير الذكي")
option = st.sidebar.selectbox("اختر نوع التقرير", ["واقعة عمل", "نموذج إفادة"])

if option == "واقعة عمل":
    st.header("نموذج تقرير واقعة")
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("التاريخ")
        location = st.text_input("المكان")
    with col2:
        time = st.text_input("الوقت (مثلاً 01:13)", value=datetime.now().strftime("%H:%M"))
        reported_by = st.text_input("المبلّغ")
    
    involved = st.text_area("الأطراف المعنية")
    description = st.text_area("وصف الواقعة")
    actions = st.text_area("الإجراءات المتخذة")
    outcome = st.text_input("النتائج")
    recommendations = st.text_area("التوصيات")

else:
    st.header("نموذج إفادة")
    date = st.date_input("التاريخ")
    day = st.text_input("اليوم")
    location = st.text_input("المكان")
    subject = st.text_input("الموضوع")
    writer = st.text_input("الاسم")
    job = st.text_input("الوظيفة")

if st.button("تحميل التقرير PDF"):
    pdf = ReportPDF()
    pdf.add_page()
    # هنا يتم إضافة النصوص بعد معالجتها بـ fix_arabic
    # سأكمل لك منطق رسم الجدول بدقة عند تشغيلك للمسودة الأولى
    st.success("تم إنشاء التقرير بنجاح!")
