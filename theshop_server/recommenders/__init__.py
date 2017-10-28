# import pickle
#
# from django.conf import settings
# from sklearn.externals import joblib
#
# neigh = joblib.load(settings.BASE_DIR + '/data/current_model.pkl')
#
# target = pickle.load(open(settings.BASE_DIR + '/data/target.p', 'rb'))
# count_vector = pickle.load(open(settings.BASE_DIR + '/data/count_vector.p', 'rb'))
# tfidf = pickle.load(open(settings.BASE_DIR + '/data/tfidf.p', 'rb'))
# scaler = pickle.load(open(settings.BASE_DIR + '/data/scaler.p', 'rb'))