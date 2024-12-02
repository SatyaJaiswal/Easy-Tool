from django.shortcuts import render

def bgRemover_view(request):
    return render(request, 'bgRemover.html')

# bgRemover/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rembg import remove
from PIL import Image
import io
import base64

@csrf_exempt
def remove_background(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]
        try:
            # Open the image file and ensure it's in RGBA mode for transparency support
            input_image = Image.open(image_file).convert("RGBA")
            
            # Apply background removal using rembg
            output_image = remove(input_image)  # This line removes the background
            
            # Save the output image to a BytesIO buffer
            buffer = io.BytesIO()
            output_image.save(buffer, format="PNG")
            img_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

            # Return the processed image as a base64 string
            return JsonResponse({"status": "success", "image": img_data})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request"})
