from tinydb import TinyDB, Query, where
import collections, os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
db = TinyDB(location + "/trustdb.json")


hostnames = []

for entity in db.search(where('news_agency')):
    hostnames.append(entity.get('news_agency'))
print(hostnames)
# print(db.search(Trust_Ratings.news_agency.news_agency))

# study1_hyper_partisan = db.search(User.study1_hyper_partisan)
# study1_main_stream = db.search(User.study1_main_stream)
# study2_fake_news = db.search(User.study2_fake_news)
# study2_hyper_partisan = db.search(User.study2_hyper_partisan)
# study2_main_stream = db.search(User.study2_main_stream)

# media_outlets = []
#
# for outlet in study1_fake_news:
#     media_outlets.append(outlet.get('study1_fake_news').get('media_agency'))
#
# for outlet in study1_hyper_partisan:
#     media_outlets.append(outlet.get('study1_hyper_partisan').get('media_agency'))
#
# for outlet in study1_main_stream:
#     media_outlets.append(outlet.get('study1_main_stream').get('media_agency'))
#
# for outlet in study2_fake_news:
#     media_outlets.append(outlet.get('study2_fake_news').get('media_agency'))
#
# for outlet in study2_hyper_partisan:
#     media_outlets.append(outlet.get('study2_hyper_partisan').get('media_agency'))
#
# for outlet in study2_main_stream:
#     media_outlets.append(outlet.get('study2_main_stream').get('media_agency'))
#
# study_1 = study1_fake_news + study1_hyper_partisan + study1_main_stream
#
# study_2 = study2_fake_news + study2_hyper_partisan + study2_main_stream
