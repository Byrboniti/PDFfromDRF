import io

from django.shortcuts import render
from rest_framework import generics
from .models import File
from .serializer import FilepdfAPISerializer, UploadSerializer

from rest_framework import generics
# from django.http import HttpResponse
# from wsgiref.util import FileWrapper
# from django.http import FileResponse
# from rest_framework import viewsets, renderers
# from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

''''''
from rest_framework import status
from rest_framework.views import APIView
from drf_pdf.response import PDFFileResponse
from drf_pdf.renderer import PDFRenderer
# from django.http import FileResponse
# from my_pdf_package import PDFGenerator

'''# from fpdf import FPDF


# class PDF(FPDF):
# 
#     def lines(self):
#         pdf_w = 210
#         pdf_h = 297
#         self.set_line_width(0.0)
#         self.line(0, pdf_h / 2, 210, pdf_h / 2)
'''



class PDFHandler(APIView):

    renderer_classes = (PDFRenderer, )

    def get(self, request):

        pdf = pdfkit.from_file(???,'foo.pdf')
        headers = {
            'Content-Disposition': 'filename="foo.pdf"',
            # 'Content-Length': len(pdf),
        }

        return Response(
            pdf,
            headers=headers,
            status=status.HTTP_200_OK
        )

class FilepdfAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FilepdfAPISerializer


# class UploadViewSet(ViewSet):
#     serializer_class = UploadSerializer
#
#     def list(self, request):
#         return Response("GET API")
#
#     def create(self, request):
#         file_uploaded = request.FILES.get('file_uploaded')
#         content_type = file_uploaded.content_type
#         response = "POST API and you have uploaded a {} file".format(content_type)
#         return Response(response)



# class PassthroughRenderer(renderers.BaseRenderer):
#
#     media_type = ''
#     format = ''
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return data
#
# class ExampleViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = File.objects.all()
#
#     @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
#     def download(self, *args, **kwargs):
#         instance = self.get_object()
#
#         # get an open file handle (I'm just using a file attached to the model for this example):
#         file_handle = instance.file.open()
#
#         # send file
#         response = FileResponse(file_handle, content_type='whatever')
#         response['Content-Length'] = instance.file.size
#         response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
#
#         return response


