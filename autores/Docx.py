from docxtpl import DocxTemplate
from models import File
import datetime as dt
from docx2pdf import convert
doc = DocxTemplate("inviteTmpl.docx")
context = File.objects.values()
print(context)
# doc.render(context)
# doc.save('invitation.docx')
# convert('invitation.docx', 'invitation.pdf')