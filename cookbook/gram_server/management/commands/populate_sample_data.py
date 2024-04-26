import uuid
import random
from django.utils import timezone
from django.core.management.base import BaseCommand
from cookbook.gram_server.models import SaleReceipt, Crops
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample crops
        crops_data = [
            {"crop_name": "Wheat", "crop_name_hi": "ghenhu", "image_thumbnail": "wheat.jpg"},
            {"crop_name": "Rice", "crop_name_hi": "chaval", "image_thumbnail": "rice.jpg"},
            {"crop_name": "Corn", "crop_name_hi": "makka", "image_thumbnail": "corn.jpg"},
            {"crop_name": "pearl", "crop_name_hi": "bhajra", "image_thumbnail": "bhajra.jpg"},
            {"crop_name": "potato", "crop_name_hi": "bateta", "image_thumbnail": "potato.jpg"},
            {"crop_name": "tomato", "crop_name_hi": "tomato", "image_thumbnail": "tomato.jpg"},
            {"crop_name": "pigeon_peas", "crop_name_hi": "toor", "image_thumbnail": "toor.jpg"},
            {"crop_name": "black_gram", "crop_name_hi": "urad", "image_thumbnail": "urad.jpg"},
            {"crop_name": "red_lentils", "crop_name_hi": "masoor", "image_thumbnail": "masoor.jpg"}
        ]

        for crop in crops_data:
            Crops.objects.create(
                crop_id=uuid.uuid4(),
                crop_name=crop['crop_name'],
                crop_name_hi=crop['crop_name_hi'],
                image_thumbnail=crop['image_thumbnail']
            )

        # Create sample sale receipts
        num_receipts = 20  # Adjust the number of receipts you want to create

        for _ in range(num_receipts):
            crop = random.choice(Crops.objects.all())
            receipt_date = timezone.now() - timezone.timedelta(days=random.randint(1, 6))
            quantity = round(random.uniform(10, 1000), 2)
            user = User.objects.filter(username="dhruvalpatel").first()
            booklet_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
            receipt_image_url = f"https://s3.amazonaws.com/receipts/{uuid.uuid4()}.jpg"
            is_approved = random.choice([True, False])
            price_updated = receipt_date - timezone.timedelta(hours=random.randint(1, 24), minutes= random.randint(1, 10))

            SaleReceipt.objects.create(
                crops=crop,
                mandi_id=random.randint(1, 100),
                mandi_name=f"Mandi_{random.randint(1, 10)}",
                mandi_name_hi=f"Mandi_{random.randint(1, 10)}",
                receipt_date=receipt_date,
                quantity=quantity,
                user=user,
                booklet_number=booklet_number,
                receipt_image_url=receipt_image_url,
                is_approved=is_approved,
                price_updated=price_updated
            )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully'))
