import google.cloud.dataflow as df
import json

# ------------------------------ Remote execution -----------------------
job_name = 'silviuc-demo'
project = 'silviuc-dataflow'
staging_location = 'gs://silviuc-dataflow/demo/staging'
temp_location = 'gs://silviuc-dataflow/demo/temp'

input_files = 'gs://silviuc-dataflow/demo/datain*'
output_prefix = 'gs://silviuc-dataflow/demo/results/out'

args = [
    '--job_name', job_name,
    '--project', project,
    '--staging_location', staging_location,
    '--temp_location', temp_location,
    '--num_workers', '5',
    '--no_save_main_session',
    '--pipeline_type_check',
    '--runner', 'BlockingDataflowPipelineRunner']
# ------------------------------ Remote execution -----------------------

class Product(object):
  def __init__(self, name, id):
    self.name = name
    self.id = id

def parse_record(e):
    r = json.loads(e)
    return Product(r['ProductName'], r['ProductID']), r['Price']

p = df.Pipeline(argv=args)

(p
 | df.io.Read(df.io.TextFileSource(input_files))
 | df.Map(parse_record)
 | df.CombinePerKey(sum)
 | df.Map(lambda (record, sales): (record.name, sales))
 | df.io.Write(df.io.TextFileSink(output_prefix)))

import logging
logging.getLogger().setLevel(logging.INFO)

p.run()
