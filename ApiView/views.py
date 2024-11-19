from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Products
from .serializer import ProductSerializer


@api_view(["GET"])
def getProducts(request):
    products = Products.objects.all()
    print(products)
    serializer = ProductSerializer(products, many=True)
    print(serializer.data)
    return Response(serializer.data)



@api_view(["POST"])
def setProducts(request):
    print("Hiiii")
    Image = request.FILES.get("image")
    name = request.data.get("name")
    description = request.data.get("description")
    price = request.data.get("price")

    print(f"Image: {Image}, Name: {name}, Description: {description}, Price: {price}")

    # Save to model
    product = Products(PImage=Image, Pname=name, Pdescription=description, Pprice=price)
    product.save()

 
    return Response({"message": "Product added successfully product"})


@api_view(["PUT"])
def updateProduct(request):
    print("Hiiii")
    Image = request.FILES.get("image")
    name = request.data.get("name")
    description = request.data.get("description")
    price = request.data.get("price")

    print(f"Image: {Image}, Name: {name}, Description: {description}, Price: {price}")

    # Update to model
    product = Products.objects.get(id=request.data.get("id"))
    product.PImage = Image
    product.Pname = name
    product.Pdescription = description
    product.Pprice = price
    product.save()

 
    return Response({"message": "Product added successfully product"})




@api_view(["DELETE"])
def deleteProduct(request):
    print("Hiiii")
    product = Products.objects.get(id=request.data.get("id"))
    product.delete()
    return Response({"message": "Product deleted successfully"})
