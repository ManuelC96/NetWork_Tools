import docx as dx 
from docx import Document
from docx.shared import Mm
# implement RMA aouto compiler
# TODO TEMPLATE class

class Template():
    
    def __init__(self, height= None, width= None, margins= None, header= None):
        self.height = height
        self.width = width
        self.margin = margins
        self.header = header
#initialize worksheet 
        self.document = dx.Document()
        self.section = self.document.sections[0]
        self.section.page_height = Mm(self.height)
        self.section.page_width = Mm(self.width)
        self.section.left_margin = Mm(self.margin)
        self.section.right_margin = Mm(self.margin)
        self.section.top_margin = Mm(self.margin)
        self.section.bottom_margin = Mm(self.margin)
        self.section.header_distance = Mm(self.header)
        self.section.footer_distance = Mm(self.header) 
# create title
    def title(self, title = str, level = int):
        self.title = title
        self.level = level
        self.document = dx.Document()
        self.document.add_heading(title, level)

# # create table
    def table(self, rows = None, cols = None):
        self.rows = rows
        self.cols = cols
        return self.document.add_table(rows=self.rows, cols=self.cols)
    
# populate table 
    def table_content(self, table = table, records= tuple):
        self.records= records
        self.table = table
    
        for a in range(len(self.records)):
            rowCells = self.table.add_row().cells

            for j in range(len(self.records[a])):
                
                if self.records[a][j]:
                    rowCells[j].text = str(self.records[a][j])
                else:
                    rowCells[j].text = input(f"inser value for:  {self.records[a][0]} ")
# save the document
    def save(self):
        
        document = self.document.save("demo.docx")
        return None

