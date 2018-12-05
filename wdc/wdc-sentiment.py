from __future__ import print_function
import json
import pandas
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features,EntitiesOptions,KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='6e8da54e-5007-4eda-aa7f-3ccbb3889f13',
  password='7F01MhpzZJGI',
  version='2018-03-16')

response = natural_language_understanding.analyze(
  text='selfdriving and electric vehicles are combining to make the cars of the future',
  features = Features(entities=EntitiesOptions(emotion=True,sentiment=True,limit=2),keywords=KeywordsOptions(emotion=True,sentiment=True))
  ).get_result()

print(response)
print(type(response))
#value = json.loads(response)
#print(type(value))
#print(value)
