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
    background-color    : qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(66, 146, 157,200), stop:1 rgba(15, 55, 55, 250));
    margin-right        : 3px;
}
QPushButton:disabled{
    background-color    : rgba(100,100,100,100);    
}
QPushButton:focus{
    border: 1px solid black;   
}
QPushButton#btn_addAuthor, #btn_addCategori, #btn_addSection,  #btn_addBookshelf {
    padding             : 2px 0px;
    border-radius       : 15px;
}


QSpinBox {
    background          : rgba(160, 230, 234, 255);
}


QStatusBar {
    color           : rgb(40,40,40);
    background-color: rgba(111, 180, 184, 255);
}

QTabWidget{

    font        : bold;
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
    background-color            : rgba(111, 180, 184, 255);
}
QTabBar::tab:last {
    border-top-right-radius     : 10px;
    border-bottom-right-radius  : 1px;
    background-color            : rgba(111, 180, 184, 255);
}
QTabBar::tab:selected{
    border-bottom   : 2px solid red;
}

QTableWidget {
    border  : 1px solid gray;
}
QTableWidget QAbstractItemView {
    font-size   : 10pt;
    font        : bold;
    color       : rgb(50,50,50);
    background  : rgb(150, 220, 224);
    selection-color: rgb(100,250,250);
    selection-background-color: rgb(90, 160, 164);
} 

"""