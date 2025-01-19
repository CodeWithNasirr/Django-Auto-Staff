from django.shortcuts import render,redirect
from .models import Image_Compression
from django.contrib import messages
from PIL import Image
from django.http import HttpResponse
import io
# Create your views here.

# def fronted_look(request):
#     print("Rendering the template...")
#     return render(request,"Image-Compression/index.html")


def image_compression(request):
    user=request.user
    if request.method=="POST":
        orginal_image = request.FILES.get("image_file")
        image_quantity= int(request.POST.get("Quality"))
        # print(f"Image:{image_file},Image_Quantity:{image_quantity}")
        x=Image_Compression(orginal_image=orginal_image,Quality=image_quantity,user=user)
        # perform compression
        img=Image.open(orginal_image)

        # # Convert RGBA to RGB if necessary
        # if img.mode == "RGBA":
        #     img = img.convert("RGB")
        output_format=img.format
        buffer=io.BytesIO()
        img.save(buffer,format=output_format,quality=image_quantity)
        buffer.seek(0)

        #Save the compression image
        x.Compress_image.save(f"Compression_{orginal_image.name}",buffer)
        x.save()
        messages.success(request, "Your Image Compressed Successfully....")

        response=HttpResponse(buffer.getvalue(),content_type=f"image/{output_format.lower()}")
        response['Content-Disposition']=f"attachment; filename=compressed_{orginal_image}"
        return response


    quality_choices = [choice[0] for choice in Image_Compression.Quality_Choices]
    context={'quality_choices':quality_choices}
    return render(request,"Image-Compression/image.html",context)
