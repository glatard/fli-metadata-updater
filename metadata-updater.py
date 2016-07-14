#!/usr/bin/env python

import argparse
import json
from pickle import dumps
from pprint import pprint

parser = argparse.ArgumentParser(description='Adds information to a JSON file.')

parser.add_argument('input_file', help='Input JSON file.')
parser.add_argument('output_file', help='Output JSON file.')
parser.add_argument('challenger_email', help='Challenger email.')
parser.add_argument('pipeline_name', help='Pipeline name.')
parser.add_argument('challenger_team_name', help='Challenger team name.')

args = parser.parse_args()

with open(args.input_file) as data_file:
  data = json.load(data_file)

data["transactionalIdentifiers"]["accountName"] = args.challenger_email
data["processingMetadata"]["pipelineName"] = args.pipeline_name
data["processingMetadata"]["challengeTeam"] = args.challenger_team_name
data["processingMetadata"]["processingPlatformInfos"] = "VIP"

f = open(args.output_file,'w')
f.write(json.dumps(data, sort_keys=True, indent=4))
f.close()


