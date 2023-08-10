import PyPDF2
from reportlab.pdfgen import canvas
from docx import Document

# 写入PDF文本的功能
def write_to_pdf(text, file_path):
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, text)  # 设置文本起始位置和内容
    c.save()
    
def prepare_text(char_name, termdict1, termdict2, HP, MOV, AGE):
    text = char_name + '\n'
    
    text += '\n'
    text += 'HP:' + '❤️ ' * HP + '\n'
    text += 'SAN:_____/' + str(termdict1['POW']) + '\n'
    text += 'MOV:' + str(MOV) + '\n'
    text += 'AGE:' + str(AGE) + '\n\n'
    
    for item in termdict1:
        new_line = item + ':   ' + str(termdict1[item]) + '\n'
        text += new_line
        
    for item in termdict2:
        new_line = item + ':   ' + str(termdict2[item]) + '\n'
        text += new_line
    

    return text
        
        
# 写入docx文件的功能
def write_to_docx(text, file_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(file_path)
    
