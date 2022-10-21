from wsgiref.util import FileWrapper
from django.http import HttpResponse
from .models import File
from .serializer import FilepdfAPISerializer
from rest_framework import generics
from rest_framework.views import APIView
from docxtpl import DocxTemplate, InlineImage
from docx2pdf import convert
from django.forms.models import model_to_dict
import pythoncom


class DocxHandler(APIView):
    def get(self, request):
        doc = DocxTemplate("inviteTmpl.docx")
        context = File.objects.get(id=1)
        u_context = model_to_dict(context)

        print(u_context)
        doc.render(u_context)
        doc.save('invitation.docx')
        pythoncom.CoInitializeEx(0)
        convert('invitation.docx', 'invitation.pdf')
        short_report = open("invitation.pdf", 'rb')
        response = HttpResponse(FileWrapper(short_report), content_type='application/pdf')
        return response


class FilepdfAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FilepdfAPISerializer
