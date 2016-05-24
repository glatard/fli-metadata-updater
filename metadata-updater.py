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

data["challengerEmail"] = args.challenger_email
data["pipelineName"] = args.pipeline_name
data["challengeTeam"] = args.challenger_team_name

f = open(args.output_file,'w')
f.write(json.dumps(data))
f.close()


