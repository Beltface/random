#!/usr/bin/env python3

import sys
import json
import time
import logging

from elasticsearch import Elasticsearch

from cortex4py.api import Api
from cortex4py.query import *

from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

class Cortex(object):
	def __init__(self):
		self.es = Elasticsearch(['127.0.0.1'], port=9200)
		self.api = Api('http://<CORTEX URL>', <CORTEX KEY>)

		self.hive_key = Nirah().config["OGMA"]["key"] 
		self.hive_api = TheHiveApi('<HIVE URL>', <HIVE KEY>, cert=False)


	def parseArtifacts(self, cortexJobId, jobId):
		artifacts = self.api.jobs.get_artifacts(cortexJobId)
		if artifacts:
			caseId = self.es.search(index='the_hive_13', body={'query':{'match':{'objectId': jobId,}}})['hits']['hits'][0]['_source']['rootId']

			for a in artifacts:
				ob = CaseObservable(dataType=a.dataType, data=a.data)
				self.hive_api.create_case_observable(caseId, ob)
				time.sleep(1)




if __name__ == "__main__":
	cor = Cortex()
	cor.parseArtifacts(sys.argv[1], sys.argv[2])
