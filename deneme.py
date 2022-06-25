import sys
from PyQt5 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc, QtPrintSupport as qtps

class InvoiceForm(qtw.QWidget):
    submitted = qtc.pyqtSignal(dict)

    def __init__(self):
        super(InvoiceForm, self).__init__()
        try:
            self.setLayout(qtw.QFormLayout())
            self.inputs = dict()
            self.inputs["Customer Name"]    = qtw.QLineEdit()
            self.inputs['Customer Adress']  = qtw.QPlainTextEdit()
            self.inputs['Invoice Date']     = qtw.QDateEdit(date= qtc.QDate.currentDate(), calendarPopup=True)
            self.inputs['Days until Due']   = qtw.QSpinBox(minimum = 0, maximum= 60, value = 30 )
            for label, widget in self.inputs.items():
                self.layout().addRow(label, widget)

            self.line_items = qtw.QTableWidget(rowCount=10, columnCount=3)
            self.line_items.setHorizontalHeaderLabels(['Job', 'Rate', 'Hours'])
            self.line_items.horizontalHeader().setSectionResizeMode( qtw.QHeaderView.Stretch )
            self.layout().addRow(self.line_items)
            for row in range(self.line_items.rowCount()):
                for col in range(self.line_items.columnCount()):
                    if col>0:
                        w = qtw.QSpinBox(minimum=0, maximum=300)
                        self.line_items.setCellWidget(row, col, w)
            submit = qtw.QPushButton("Create Invoice", clicked=self.on_submit)
            self.layout().addRow(submit)
            self.on_submit()
        except Exception as E:
            print("class InvoiceForm init fonk")

    def on_submit(self):
        try:
            data = {
                'c_name'    : self.inputs['Customer Name'].text(),
                'c_addr'    : self.inputs['Customer Adress'].toPlainText(),
                'i_date'    : self.inputs['Invoice Date'].date().toString(),
                'i_due'     : self.inputs['Invoice Date'].date().addDays(self.inputs['Days until Due'].value()).toString(),
                'i_terms'   : '{} days'.format( self.inputs['Days until Due'].value() )            }
            data['line_items'] = list()
            for row in range( self.line_items.rowCount() ):
                if not self.line_items.item(row, 0):
                    continue
                job     = self.line_items.item(row, 0).text()
                rate    = self.line_items.cellWidget(row, 1).value()
                hours   = self.line_items.cellWidget(row, 2).value()
                total   = rate * hours
                row_data= [job, rate, hours, total]
                if any(row_data):
                    data['line_items'].append(row_data)
            data['total_due'] = sum(x[3] for x in data["line_items"])
            self.submitted.emit(data)
        except Exception as E:
            print("Fonk: on_submit")

class InvoiceView(qtw.QTextEdit):
    dpi         = 72
    doc_width   = int(8.5 * dpi)
    doc_height  = int(11 * dpi)

    def __init__(self):
        try:
            super(InvoiceView, self).__init__(readOnly=True)
            self.setFixedSize( qtc.QSize(self.doc_width, self.doc_height ))
        except Exception as E:
            print("Fonk: class InvoiceView init")

    def set_page_size(self, qrect):
        try:
            self.doc_width = int(qrect.width())
            self.doc_height= int(qrect.height())
            self.setFixedSize(qtc.QSize(self.doc_width, self.doc_height))
            self.document().setPageSize( qtc.QSizeF(self.doc_width, self.doc_height))
        except Exception as E:
            print("Fonk: set_page_size")

    def build_invoice(self, data):
        try:
            document = qtg.QTextDocument()
            self.setDocument(document)
            document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
            cursor = qtg.QTextCursor(document)
            root = document.rootFrame()
            cursor.setPosition(root.lastPosition())

            # Insert top level frames
            logo_frame_fmt = qtg.QTextFrameFormat()
            logo_frame_fmt.setBorder(2)
            logo_frame_fmt.setPadding(10)
            logo_frame_fmt.setLeftMargin(20)
            logo_frame_fmt.setRightMargin(20)
            logo_frame_fmt.setBackground(qtg.QColor("cyan"))
            logo_frame = cursor.insertFrame(logo_frame_fmt)

            cursor.setPosition(root.lastPosition())
            cust_addr_frame_fmt = qtg.QTextFrameFormat()
            cust_addr_frame_fmt.setWidth(self.doc_width * .3)
            cust_addr_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatRight)
            cust_addr_frame =  cursor.insertFrame(cust_addr_frame_fmt)

            cursor.setPosition(root.lastPosition())
            terms_frame_fmt = qtg.QTextFrameFormat()
            terms_frame_fmt.setWidth(self.doc_width * .5)
            terms_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
            terms_frame = cursor.insertFrame(terms_frame_fmt)

            cursor.setPosition(root.lastPosition())
            line_items_frame_fmt = qtg.QTextFrameFormat()
            line_items_frame_fmt.setMargin(25)
            line_items_frame = cursor.insertFrame(line_items_frame_fmt)

            # Create the heading
            # create a format for the characters
            std_format = qtg.QTextCharFormat()

            logo_format = qtg.QTextCharFormat()
            logo_format.setFont(qtg.QFont('Arial', 18, qtg.QFont.DemiBold))
            logo_format.setUnderlineStyle(qtg.QTextCharFormat.SingleUnderline)
            logo_format.setVerticalAlignment(qtg.QTextCharFormat.AlignMiddle)


            label_format = qtg.QTextCharFormat()
            label_format.setFont(qtg.QFont("Sans", 12, qtg.QFont.Bold))

            # create a format for the block
            cursor.setPosition(logo_frame.firstPosition())

            # The easy way
            # cursor.insertImage('logo.png')
            # Better way
            logo_image_fmt = qtg.QTextImageFormat()
            logo_image_fmt.setName("img/logo.jpg")
            logo_image_fmt.setHeight(48)
            logo_image_fmt.setWidth(64)
            cursor.insertImage(logo_image_fmt, qtg.QTextFrameFormat.FloatRight)
            cursor.insertText("Necip Fazıl Ortaokulu", logo_format)
            # cursor.insertBlock()
            # cursor.insertText("Adres: Belde Mah. BATMAN 72070", std_format)

            # customer adress
            cursor.setPosition(cust_addr_frame.lastPosition())
            addess_format = qtg.QTextBlockFormat()
            addess_format.setBackground(qtg.QColor("gray"))
            addess_format.setLineHeight(150, qtg.QTextBlockFormat.ProportionalHeight)
            addess_format.setAlignment(qtc.Qt.AlignRight)
            addess_format.setRightMargin(25)

            cursor.insertBlock(addess_format)
            cursor.insertText("Customer:", label_format)
            cursor.insertBlock(addess_format)
            cursor.insertText(data["c_name"], std_format)
            cursor.insertBlock(addess_format)
            cursor.insertText(data["c_addr"])

            # Terms
            cursor.setPosition(terms_frame.lastPosition())
            cursor.insertText("Terms:", label_format)
            cursor.insertList(qtg.QTextListFormat.ListCircle)       # liste elemanlarının başındaki işareti belirler
            # cursor is now in the first list item

            term_items = (
                f"<b>Invoice dated :</b> {data['i_date']}",
                f"<b>Invoice terms :</b> {data['i_terms']}",
                f"<b>Invoice due   :</b> {data['i_due']}"  )

            for i, item in enumerate(term_items):
                if i>0:
                    cursor.insertBlock()
                # we can insert HTML too, but not with a textformat
                cursor.insertHtml(item)

            # line items
            table_format = qtg.QTextTableFormat()
            table_format.setHeaderRowCount(1)
            table_format.setWidth(
                qtg.QTextLength( qtg.QTextLength.PercentageLength, 100))             # Tablo sütun genişliği

            headings = ('Job', 'Rate', 'Hours', 'Cost')
            num_rows = len(data['line_items'])+1
            num_cols = len(headings)

            cursor.setPosition(line_items_frame.lastPosition())
            table = cursor.insertTable(num_rows, num_cols, table_format)

            # now we are in the first cell of the table
            # write headers
            for heading in headings:
                cursor.insertText(heading, label_format)
                cursor.movePosition(qtg.QTextCursor.NextCell)

            # write data
            for row in data['line_items']:
                for col, value in enumerate(row):
                    text = f"${value}" if col in (1,3) else f"{value}"
                    cursor.insertText(text, std_format)
                    cursor.movePosition(qtg.QTextCursor.NextCell)

            # Append a row
            table.appendRows(1)
            cursor = table.cellAt(num_rows, 0).lastCursorPosition()
            cursor.insertText('Total', label_format)
            cursor = table.cellAt(num_rows, 3).lastCursorPosition()
            cursor.insertText(f"${data['total_due']}", label_format)
        except Exception as E:
            print(f"fonk: build_invoice {E}")


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """Mainwindow constructor"""
        super(MainWindow, self).__init__()
        # Main UI code goes here
        layout = qtw.QHBoxLayout(self)
        mainWidget = qtw.QWidget()
        self.setCentralWidget(mainWidget)
        mainWidget.setLayout(layout)

        form = InvoiceForm()
        mainWidget.layout().addWidget(form)

        self.preview = InvoiceView()
        mainWidget.layout().addWidget(self.preview)

        form.submitted.connect(self.preview.build_invoice)

        try:
            # printing
            print_tb = self.addToolBar("Printing")
            print_tb.addAction("Configure Printer", self.printer_config)
            print_tb.addAction("Print Preview", self.print_preview)
            print_tb.addAction("Print dialog", self.print_dialog)
            print_tb.addAction("Export PDF", self.export_pdf)

            self.printer = qtps.QPrinter()
            # Configure defaults:
            self.printer.setOrientation(qtps.QPrinter.Portrait)
            self.printer.setPageSize(qtg.QPageSize(qtg.QPageSize.A4))
        except Exception as E:
            print(f"Hata Alanı 1: {E}")

        # End main UI code
        self.show()

    def _update_preview_size(self):
        try:
            self.preview.set_page_size(self.printer.pageRect(qtps.QPrinter.Point))
        except Exception as E:
            print(f"Hata Alanı 2: {E}")

    def printer_config(self):
        try:
            dialog = qtps.QPageSetupDialog(self.printer, self)
            dialog.exec_()
            self._update_preview_size()
        except Exception as E:
            print(f"Hata Alanı 3: {E}")

    def _print_document(self):
        # doesn't actually kick off printer
        # just paints document to the printer object
        try:
            self.preview.document().print(self.printer)
        except Exception as E:
            print(f"Hata Alanı 4: {E}")

    def print_dialog(self):
        try:
            self._print_document()
            dialog = qtps.QPrintDialog(self.printer, self)
            dialog.exec_()
            self._update_preview_size()
        except Exception as E:
            print(f"Hata Alanı 5: {E}")

    def print_preview(self):
        try:
            dialog = qtps.QPrintPreviewDialog(self.printer, self)
            dialog.paintRequested.connect(self._print_document)
            dialog.exec_()
            self._update_preview_size()
        except Exception as E:
            print(f"Hata Alanı 6: {E}")

    def export_pdf(self):
        try:
            filename, _ = qtw.QFileDialog.getSaveFileName(
                self, "Save to PDF", qtc.QDir.homePath(), "PDF Files (*.pdf)"  )
            if filename:
                self.printer.setOutputFileName(filename)
                self.printer.setOutputFormat(qtps.QPrinter.PdfFormat)
                self._print_document()
        except Exception as E:
            print(f"Hata Alanı 7: {E}")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw  = MainWindow()
    sys.exit(app.exec_())










