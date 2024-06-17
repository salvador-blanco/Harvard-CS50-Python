from fpdf import FPDF
def main():

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    image_path = "shirtificate.png"
    pdf.image(image_path, x=0, y=25)

    user_name = input("Name: ")
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 70, user_name + " took CS50", border=False, ln=1, align = 'C')

    pdf.output("shirtificate.pdf")


class PDF(FPDF):

    def header(self):
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, 'shirtificate', border=False, ln=1, align ='C')
        self.ln(20)

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
