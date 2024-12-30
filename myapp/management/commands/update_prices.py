from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = 'Update all product prices by dividing them by 100'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            product.orignal_price /= 100  # Use 'original_price' instead of 'price'
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Updated product {product.id} original price to {product.orignal_price}')) 