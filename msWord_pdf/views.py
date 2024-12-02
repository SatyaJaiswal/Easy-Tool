from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from docx import Document
import pdfkit
import os
from tempfile import NamedTemporaryFile

def msWord_pdf(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        if not uploaded_file.name.endswith(('.doc', '.docx')):
            return JsonResponse({'error': 'Invalid file format. Please upload a .doc or .docx file.'}, status=400)

        try:
            # Read Word file content
            doc = Document(uploaded_file)
            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    p { margin: 10px 0; }
                </style>
            </head>
            <body>
            """
            for paragraph in doc.paragraphs:
                html_content += f"<p>{paragraph.text}</p>"
            html_content += "</body></html>"

            # Specify the correct path to wkhtmltopdf for Windows
            wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Make sure this is the correct path
            pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

            # Create a temporary file to store the PDF output
            with NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                pdfkit.from_string(html_content, temp_pdf.name, configuration=pdfkit_config)

            # Open the temporary file to read it back
            with open(temp_pdf.name, 'rb') as f:
                pdf_data = f.read()

            # Clean up the temporary file after reading it
            os.remove(temp_pdf.name)

        except Exception as e:
            return JsonResponse({'error': f"Error during conversion: {str(e)}"}, status=500)

        # Return the PDF file as an HTTP response
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="converted.pdf"'
        return response

    return render(request, 'msWord_pdf.html')
