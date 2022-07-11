mystyle = """
QCheckBox::indicator {
    background-color: rgba(160, 230, 234, 255);
    border  : 1px solid pink;
}
QCheckBox::indicator:checked {    
    background-color: rgba(66,146,157,255);
    
}

QComboBox {     
    font-size   : 10pt ;
    padding     : 0 10px;
    color       : rgb(50, 50, 50);
    background  : rgba(160, 230, 234, 255);
} 

QComboBox QAbstractItemView {
    color       : rgb(50,50,50);
    background  : rgb(150, 220, 224);
    selection-color: rgb(100,250,250);
    selection-background-color: rgb(90, 160, 164);
    padding     : 5px;
}     
QComboBox:disabled { 
    font-size   : 10pt;
    color       : rgb(200,200,200);
    background  : gray;
}
QComboBox:editable {
    color           : rgb(20,20,20);    
    background      : rgba(160, 230, 234, 255);
    selection-color : rgb(25,250,250);
    selection-background-color: gray;
}

QDateEdit {
    font-size: 10pt ;
    padding: 0 10px;
    color: rgb(50, 50, 50);
    background  : rgba(160, 230, 234, 255);   
}
QDateEdit QAbstractItemView {
    color       : rgb(50,50,50);
    background  : rgb(150, 220, 224);
    selection-color: rgb(100,250,250);
    selection-background-color: rgb(90, 160, 164);
    padding  : 5px;
} 


QInputDialog {
    background  : #e2f0f1;
    font-size   : 10pt;
}


QFrame {
    border  : none;
}
QFrame#frame_login1 {
    background      : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(15, 55, 55, 255));
    color           : white; 
    border          : None; 
    border-radius   : 15px; 
    font            : bold; 
    font-size       : 10pt; 
    padding         : 10px 10px;
}


QGroupBox {
    border  : none;    
}
QGroupBox#groupBox_category, #groupBox_author, #groupBox_section, #groupBox_bookshelf {     
    padding : 25px 0px 0px 0px;
}
QGroupBox::title {   
    font                    : italic bold 10pt;                       
    border-top-right-radius : 15px;
    border-top-left-radius  : 15px;
    subcontrol-origin       : margin;
    subcontrol-position     : top center;
    padding                 : 3px 40px 3px 40px;
    background-color        : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
    color                   : rgb(250, 250, 250);
}
QGroupBox#groupBox_uyeBilgileri, #groupBox_verilenler, #groupBox_1, #groupBox_2, #groupBox_3, #groupBox_4, #groupBox_5  {
    padding : 10px 10px 0px 10px; 
    font    : italic bold 10pt;
    border  : 1px solid gray;
    border-radius: 5px;
}
QGroupBox::title#groupBox_uyeBilgileri, ::title#groupBox_verilenler, 
::title#groupBox_1, ::title#groupBox_2, ::title#groupBox_3, ::title#groupBox_4, ::title#groupBox_5  {                             
    border-top-right-radius : 15px;
    border-top-left-radius  : 15px;
    subcontrol-origin       : margin;
    subcontrol-position     : top center;
    padding                 : 4px 40px 4px 40px;
    background-color        : green;
    color                   : rgb(250, 250, 250);    
}


QLineEdit{
    border: 1px solid gray;
    background: rgba(160, 230, 234, 255);
    border-radius: 5px;
    padding: 0px 10px;
}
QLineEdit:focus{
    border: 1px solid black;
}
QLineEdit#le_searchOutsides, #le_searchExpired, #le_searchGivenToday, #le_searchMember, #le_searchBook, #le_kategori, #le_author, #le_section, #le_bookshelf {
    border: 1px solid gray;
    background: rgba(160, 230, 234, 255);
    border-radius: 5px;
    padding: 0px 10px;
}
QLineEdit#le_searchOutsides:focus, #le_searchExpired:focus, #le_searchGivenToday:focus, #le_searchMember:focus, #le_searchBook:focus, 
#le_searchBarcode:focus, #le_kategori:focus, #le_author:focus, #le_section:focus, #le_bookshelf:focus{
    border: 1px solid black;    
}

QListWidget {
    background: rgba(160, 230, 234, 255);
}
QListWidget::item:selected {
    background-color: rgb(90, 160, 164);
}

QMainWindow {
    background  : #e2f0f1;             
}

QMessageBox {
    background  : #e2f0f1;
}


QPlainTextEdit {
    border: 1px solid gray;
    background: rgba(160, 230, 234, 255);
    border-radius: 5px;
    padding: 0px 10px;
}
QPlainTextEdit:focus{
    border: 1px solid black;
}

QPushButton{
    background-color    : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
    color               : white; 
    border              : None; 
    border-radius       : 5px; 
    font                : bold; 
    font-size           : 10pt; 
    padding             : 2px 10px;
}
QPushButton:hover{
    background-color    : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 205), stop:1 rgba(75, 115, 135, 205));
    margin-right        : 3px;
}
QPushButton:disabled{
    background-color    : rgba(100,100,100,100);    
}
QPushButton:focus{
    border: 1px solid black;   
}
QPushButton#btn_addAuthor, #btn_addCategori, #btn_addSection,  #btn_addBookshelf {
    padding             : 0px 0px;
    border-radius       : 10px;
    margin-left         : 4px;
}


QSpinBox {
    background          : rgba(160, 230, 234, 255);
}


QScrollBar:vertical {
    min-width   : 15px;
    max-width   : 20px;
    border      : 1px solid gray;
    margin      : 20px 0px 20px 0px;
}
QScrollBar::add-line:vertical {
    border                      : 1px solid gray;
    border-bottom-right-radius  : 3px;
    border-bottom-left-radius   : 3px;
    background                  : #9acbcd;
    height                      : 20px;
    subcontrol-position         : bottom;
    subcontrol-origin           : margin;
}
QScrollBar::add-line:vertical:hover {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
}
QScrollBar::add-line:vertical:pressed {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 155), stop:1 rgba(75, 115, 135, 155));
}
QScrollBar::sub-line:vertical {                 
      border                    : 1px solid gray;
      border-top-right-radius   : 3px;
      border-top-left-radius    : 3px;
      background                : #9acbcd;
      height                    : 20px;
      subcontrol-position       : top;
      subcontrol-origin         : margin;
}
QScrollBar::sub-line:vertical:hover {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
}
QScrollBar::sub-line:vertical:pressed {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 155), stop:1 rgba(75, 115, 135, 155));
}
QScrollBar::handle:vertical {
    border-top                  : 1px solid gray;
    border-bottom               : 1px solid gray;
    background                  : #9acbcd;
    border-radius               : 1px;
    min-height                  : 10px;
}
QScrollBar::handle:vertical:hover {
    background                  : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
}
QScrollBar::up-arrow:vertical {
      border                    : 1px solid gray;
      border-top-left-radius    : 5px;
      border-top-right-radius   : 5px;
      width                     : 8px;
      height                    : 8px;
      background                : white;
}
QScrollBar::down-arrow:vertical {
      border                    : 1px solid gray;
      border-bottom-left-radius : 5px;
      border-bottom-right-radius: 5px;
      width                     : 8px;
      height                    : 8px;
      background                : white;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
      background    : rgb(200,230,230);
}


QScrollBar:horizontal {
    min-height   : 15px;
    max-height   : 20px;
    border      : 1px solid gray;
    margin      : 0px 20px 0px 20px;
}
QScrollBar::sub-line:horizontal {
    border                      : 1px solid gray;
    border-left-top-radius      : 3px;
    border-left-bottom-radius   : 3px;
    background                  : #9acbcd;
    width                       : 20px;
    subcontrol-position         : left;
    subcontrol-origin           : margin;
}
QScrollBar::sub-line:horizontal:hover {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
}
QScrollBar::sub-line:horizontal:pressed {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 155), stop:1 rgba(75, 115, 135, 155));
}
QScrollBar::add-line:horizontal {                 
      border                    : 1px solid gray;
      border-right-top-radius   : 3px;
      border-right-bottom-radius: 3px;
      background                : #9acbcd;
      width                     : 20px;
      subcontrol-position       : right;
      subcontrol-origin         : margin;
}
QScrollBar::add-line:horizontal:hover {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
}
QScrollBar::add-line:horizontal:pressed {
      background                : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 155), stop:1 rgba(75, 115, 135, 155));
}
QScrollBar::handle:horizontal {
    border-left                 : 1px solid gray;
    border-right                : 1px solid gray;
    background                  : #9acbcd;
    border-radius               : 1px;
    min-width                   : 10px;
}
QScrollBar::handle:horizontal:hover {
    background                  : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(66, 146, 157, 255), stop:1 rgba(75, 115, 135, 255));
}
QScrollBar::left-arrow:horizontal {
      border                    : 1px solid gray;
      border-top-left-radius    : 5px;
      border-bottom-left-radius : 5px;
      width                     : 8px;
      height                    : 8px;
      background                : white;
}
QScrollBar::right-arrow:horizontal {
      border                    : 1px solid gray;
      border-top-right-radius   : 5px;
      border-bottom-right-radius: 5px;
      width                     : 8px;
      height                    : 8px;
      background                : white;
}
QScrollBar::sub-page:horizontal, QScrollBar::add-page:horizontal {
      background    : rgb(200,230,230);
}


QStatusBar {
    color           : rgb(40,40,40);
    background-color: rgba(111, 180, 184, 255);
}

QTabWidget{
    font            : bold;
    background-color: rgba(111, 180, 184, 255);
}
QTabWidget::pane{
    background-color: rgba(111, 180, 184, 255);
    border-radius   : 15px;
}
QTabWidget::tab-bar{
    alignment       : center;
    background-color: rgba(111, 180, 184, 255);
}
QTabBar::tab {
    padding     : 5px 30px;
    color       : black;
    background  : rgba(111, 180, 184, 255);
    margin      : 1px;
    font-size   : 10pt;
}
QTabBar::tab:first {
    border-top-left-radius      : 10px;
    border-bottom-left-radius   : 1px;
}
QTabBar::tab:last {
    border-top-right-radius     : 10px;
    border-bottom-right-radius  : 1px;
}
QTabBar::tab:selected{
    border-bottom   : 2px solid red;
}

QTableWidget {
    border  : 1px solid gray;
}
QTableWidget::item {
    background  : rgb(230,255,255);
}
QTableWidget::item:selected {
    background  : rgb(150, 220, 224);
    color       : black;
}
QTableWidget QAbstractItemView {
    font-size   : 10pt;
    font        : bold;
    color       : rgb(50,50,50);
    background  : rgb(150, 220, 224);
    selection-color: rgb(100,250,250);
    selection-background-color: rgb(90, 160, 164);
} 
QTableWidget QTableCornerButton::section {
    background  : rgb(150, 220, 224);
}

"""