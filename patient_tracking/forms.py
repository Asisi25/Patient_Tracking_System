from django import forms
from .models import Patient;

class PatientForm(forms.Form): 
    name = forms.CharField(min_length=2, max_length=150, required=True,
        error_messages={
            'min_length': 'Shop name should be at least 2 character',
            'required': "Please enter your shop name"
        }
    )
    volume = forms.DecimalField(max_digits=19, decimal_places=10, initial=0.01, min_value=0.01, required=True,
        error_messages={
            'min_value': 'Product volume cannot be less than 0.01',
            'required': "Please enter  product volume"
        }
    )
    weight = forms.DecimalField(max_digits=19, decimal_places=10, initial=0.01, min_value=0.01, required=True,
        error_messages={
            'min_value': 'Product weight cannot be less than 0.01',
            'required': "Please enter  product volume"
        }
    )
    price = forms.DecimalField(max_digits=19, decimal_places=10, initial=0, min_value=0, required=True,
        error_messages={
            'min_value': 'Product price cannot be less than 0',
            'required': "Please enter  product price"
        }
    )    
   
    def clean(self):
        self.cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        volume = self.cleaned_data.get('volume')
        weight = self.cleaned_data.get('weight')
        categories = self.cleaned_data.get('categories')
        quantity = self.cleaned_data.get('quantity')
        description =self.cleaned_data.get('description')
    def save(self, request): 
        shop = request.user.shop
        name = self.cleaned_data["name"]
        volume = self.cleaned_data['volume']
        weight = self.cleaned_data['weight']
        categories = self.cleaned_data['categories']
        images = request.FILES.getlist('images')
        quantity = self.cleaned_data['quantity']
        attributes = self.cleaned_data['attributes']
        description = self.cleaned_data['description']
        price = self.cleaned_data['price']

        # product = Product.objects.create(shop=shop, name=name, volume=volume, weight=weight, description=description, price=price)
        # for image in images:
        #     photo = Photo.objects.create(image=image)
        #     product.photos.add(photo)

        # for category in categories:
        #     if ObjectId.is_valid(category) and Category.objects.get(pk=ObjectId(category)) is not None:
        #         product.categories.add( Category.objects.get(pk=ObjectId(category))) 
        #         product.save()
        
        # inventory = ProductInventory.objects.create(quantity=quantity)

        # for attribute in attributes:
        #     if ObjectId.is_valid(attribute) and Attribute.objects.get(pk=ObjectId(attribute)) is not None:
        #         inventory.attributes.add( Attribute.objects.get(pk=ObjectId(attribute))) 
        #         inventory.save()

        # product.inventories.add(inventory)
        # return product
