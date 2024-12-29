import random
import os
import django
from django.utils.text import slugify

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from myapp.models import Product, Category, Company

def add_mobile_products():
    try:
        # Get Mobile Phones category - using the exact name from companyScript.py
        mobile_category = Category.objects.get(category="Mobile Phones")
        
        # Folder path containing mobile images
        image_folder = r"C:\Users\Lenovo\Downloads\Programs\mobilephotosrandom\images"

        # Get all companies associated with the Mobile category
        mobile_companies = Company.objects.filter(category=mobile_category)

        if not mobile_companies.exists():
            print("No mobile companies found! Please run companyScript.py first.")
            return

        # Example product descriptions
        mobile_descriptions = [
            "A high-performance mobile with the latest technology.",
            "Compact and stylish mobile, perfect for everyday use.",
            "Affordable mobile with excellent camera and battery life.",
            "Top-notch mobile with unbeatable features and performance."
        ]

        # Loop through the images in the folder and create products
        for image_name in os.listdir(image_folder):
            if image_name.endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Randomly select a company
                    company = random.choice(mobile_companies)

                    # Generate product details
                    product_name = os.path.splitext(image_name)[0].replace('_', ' ').title()
                    description = random.choice(mobile_descriptions)
                    original_price = random.randint(500, 2000)  # More realistic price range
                    discount_percentage = random.randint(5, 30)  # More realistic discount range

                    # Create the Product instance
                    Product.objects.create(
                        category=mobile_category,
                        company=company,
                        product_name=product_name,
                        product_description=description,
                        orignal_price=original_price,
                        discount_percentage=discount_percentage,
                        warranty=random.randint(1, 2),  # 1-2 years warranty
                        product_image=f"product_images/{image_name}",
                        is_stock=True,
                        is_active=True,
                        is_trending=random.choice([True, False]),
                        slug=slugify(product_name)
                    )
                    print(f"Added product: {product_name}")
                except Exception as e:
                    print(f"Error adding {image_name}: {str(e)}")

    except Category.DoesNotExist:
        print("Mobile Phones category not found! Please run companyScript.py first.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Adding mobile products...")
    add_mobile_products()
    print("Done!")
