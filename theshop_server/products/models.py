# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from mongoengine import Document
from mongoengine.fields import StringField, DateTimeField, FloatField, BooleanField


class Product(Document):
    uniq_id = StringField()
    crawl_timestamp = DateTimeField()

    product_url = StringField()
    product_name = StringField()
    product_category_tree = StringField()

    pid = StringField()
    retail_price = FloatField()
    discounted_price = FloatField()

    image = StringField()
    is_FK_Advantage_product = BooleanField()

    description = StringField()
    product_rating = FloatField()
    overall_rating = FloatField()

    brand = StringField()
    product_specifications = StringField()

    @property
    def data(self):
        _data = json.loads(self.to_json())
        special = {}
        product_specifications = json.loads(_data['product_specifications'].replace('=>', ':'))
        for product_specification in product_specifications['product_specification']:
            special[product_specification['key'] if product_specification.get('key') else product_specification['value']] = \
                product_specification['value']
        first_image = json.loads(_data['image'])
        if first_image:
            first_image = first_image[0]
            special['first_image'] = first_image
        _data.update(special)
        return _data

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        # TODO: Update recommendation model
        pass

