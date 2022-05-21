from fpdf import FPDF

title = '20000 Leagues Under the Seas'

class PDF(FPDF):
    def header(self):
        # helvetica bold 15
        self.set_font('helvetica', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True,)


        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # helvetica italic 8
        self.set_font('helvetica', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no())+"/{nb}", new_x="LMARGIN", new_y="NEXT", align="C", fill=True)

    def chapter_title(self, num, label):
        # helvetica 12
        self.set_font('helvetica', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt, new_x="LMARGIN", new_y="NEXT")
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

pdf = PDF()
pdf.set_title(title)
pdf.set_author('Jules Verne')
pdf.print_chapter(1, 'A RUNAWAY REEF', 'txt/20k_c1.txt')
pdf.print_chapter(2, 'THE PROS AND CONS', 'txt/20k_c2.txt')
pdf.output("C:\\Users\\msero\\Desktop\\tuto3.pdf")

