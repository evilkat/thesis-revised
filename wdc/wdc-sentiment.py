from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features,EntitiesOptions,KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='6e8da54e-5007-4eda-aa7f-3ccbb3889f13',
  password='7F01MhpzZJGI',
  version='2018-03-16')

response = natural_language_understanding.analyze(
  text='IBM is an American multinational technology company ' 
       'headquartered in Armonk, New York, United States, ' 
       'with operations in over 170 countries.',
  features = Features(entities=EntitiesOptions(emotion=True,sentiment=True,limit=2),keywords=KeywordsOptions(emotion=True,sentiment=True,limit=2))
  ).get_result()

#print(response)
print(json.dumps(response))