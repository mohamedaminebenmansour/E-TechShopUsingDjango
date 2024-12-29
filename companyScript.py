import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from myapp.models import Category, Company

def create_categories_and_companies():
    # Create categories
    mobile_phones = Category.objects.create(category="Mobile Phones")
    laptops = Category.objects.create(category="Laptops")
    tablets = Category.objects.create(category="Tablet")

    # Create companies for Mobile Phones
    mobile_companies = [
        "Apple",
        "Samsung",
        "Xiaomi",
        "Huawei",
        "OnePlus",
        "Google"
    ]
    
    # Create companies for Laptops
    laptop_companies = [
        "Apple",
        "Dell",
        "HP",
        "Lenovo",
        "Asus",
        "Acer"
    ]
    
    # Create companies for Tablets
    tablet_companies = [
        "Apple",
        "Samsung",
        "Microsoft",
        "Lenovo",
        "Huawei"
    ]

    # Add companies with their categories
    for company_name in mobile_companies:
        Company.objects.create(category=mobile_phones, company=company_name)
    
    for company_name in laptop_companies:
        Company.objects.create(category=laptops, company=company_name)
        
    for company_name in tablet_companies:
        Company.objects.create(category=tablets, company=company_name)

if __name__ == "__main__":
    print("Creating categories and companies...")
    create_categories_and_companies()
    print("Done!")
