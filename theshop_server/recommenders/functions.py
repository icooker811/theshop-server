import numpy as np
import pandas as pd
import pickle
from django.conf import settings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import NearestNeighbors

from sklearn import preprocessing

from sklearn.externals import joblib

from theshop_server import count_vector, tfidf, scaler, target, neigh

from products.models import *


def build_product_recommendation_model():
    data = []
    for product in Product.objects.all():
        data.append({
            'description': product.to_text,
            'uniq_id': product.uniq_id,
            'discounted_price': product.discounted_price
        })

    products = pd.read_json(json.dumps(data))
    products = products[['uniq_id', 'description', 'discounted_price']].dropna()
    target = products.iloc[:, 0].values

    count_vector = CountVectorizer()
    count_array = count_vector.fit_transform(products['description'])

    tfidf = TfidfTransformer()
    tfidf_vector = tfidf.fit_transform(count_array)
    tfitf_array = tfidf_vector.toarray()

    scaler = preprocessing.Normalizer().fit(products['discounted_price'])
    new_retail_price = scaler.transform(products['discounted_price'])

    new_feature = np.concatenate([tfitf_array, np.reshape(new_retail_price, [-1, 1])], axis=1)

    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(new_feature)

    pickle.dump(target, open(settings.BASE_DIR + '/data/target.p', 'wb'))

    pickle.dump(count_vector, open(settings.BASE_DIR + '/data/count_vector.p', 'wb'))
    pickle.dump(tfidf, open(settings.BASE_DIR + '/data/tfidf.p', 'wb'))
    pickle.dump(scaler, open(settings.BASE_DIR + '/data/scaler.p', 'wb'))

    joblib.dump(neigh, settings.BASE_DIR + 'data/current_model.pkl')


def get_product_recommendation(keyword, price=1000.0):

    p_count_array = count_vector.transform([keyword])
    p_tfidf_vector = tfidf.transform(p_count_array)
    p_tfitf_array = p_tfidf_vector.toarray()

    p_new_price = scaler.transform(price)
    p_new_feature = np.concatenate([p_tfitf_array, np.reshape([p_new_price], [-1, 1])], axis=1)

    p_data = scaler.transform(p_new_feature)
    distance, best_n = neigh.kneighbors(p_data, return_distance=True)

    best_target = []
    for n in best_n:
        best_target.append(target[n])

    best_target = list(best_target)
    best_target = [best_target[0][0], best_target[0][1], best_target[0][2]]
    return Product.objects.filter(uniq_id__in=best_target)
