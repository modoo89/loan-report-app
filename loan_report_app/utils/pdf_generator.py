from fpdf import FPDF
import os

def create_pdf_report(info, df):
    pdf = FPDF()
    pdf.add_page()
    font_path = os.path.join("fonts", "NanumGothic.ttf")
    pdf.add_font("Nanum", "", font_path, uni=True)
    pdf.set_font("Nanum", "", 12)

    pdf.cell(0, 10, "■ 고객정보", ln=True)
    for k, v in info.items():
        pdf.cell(0, 8, f"◆ {k}: {v}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 10, "■ 상품별 대출 시뮬레이션 리포트", ln=True)

    cols = df.columns.tolist()
    col_width = pdf.w / len(cols) - 10
    for col in cols:
        pdf.cell(col_width, 8, col, border=1)
    pdf.ln()
    for _, row in df.iterrows():
        for item in row:
            pdf.cell(col_width, 8, str(item), border=1)
        pdf.ln()

    output_path = "대출_리포트.pdf"
    pdf.output(output_path)
    return output_path