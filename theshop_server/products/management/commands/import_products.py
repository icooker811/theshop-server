# -*- encoding: utf-8 -*-


from django.core.management.base import BaseCommand, CommandError
from common.functions import get_data_from_csv
from products.models import Product


class Command(BaseCommand):
    args = 'data.csv'
    help = 'Import Data'

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):

        if not options:
            raise CommandError('Please input path')

        file_path = options['file_path']

        data = get_data_from_csv(file_path)

        length = len(data)

        i = 0
        for row in data:
            i += 1
            value = {
                'uniq_id': row['uniq_id'],
                'crawl_timestamp': row['crawl_timestamp'],
                'product_url': row['product_url'],
                'product_name': row['product_name'],
                'product_category_tree': row['product_category_tree'],
                'pid': row['pid'],
                'retail_price': row['retail_price'] if row['retail_price'] != '' else None,
                'discounted_price': row['discounted_price'] if row['discounted_price'] != '' else None,
                'image': row['image'],
                'is_FK_Advantage_product': row['is_FK_Advantage_product'],
                'description': row['description'],
                'product_rating': row['product_rating'] if row['product_rating'] != 'No rating available' else None,
                'overall_rating': row['overall_rating'] if row['overall_rating'] != 'No rating available' else None,
                'brand': row['brand'],
                'product_specifications': row['product_specifications'],
            }

            product = Product.objects.create(**value)
            print ('(', i, '/', length, ')', product.uniq_id)



