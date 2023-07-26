"""program prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf"""

from fpdf import FPDF


class Shirtificate(FPDF):
    name = input("Name: ")
    top_title = "CS50 Shirtificate"
    image_way = r'shirtificate.png'

    def title(self):
        self.add_page()
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, txt=Shirtificate.top_title, new_x="LMARGIN", new_y="NEXT", align='C')

    def add_shirt(self):
        self.image(Shirtificate.image_way, w=self.epw)

    def add_name(self):
        self.set_font_size(25)
        self.set_text_color(255,255,255)
        self.text(59, 136, f"{Shirtificate.name} took CS50")


shirtificate = Shirtificate()
shirtificate.title()
shirtificate.add_shirt()
shirtificate.add_name()
shirtificate.output("shirtificate.pdf")
