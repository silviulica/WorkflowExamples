import google.cloud.dataflow as df
import json

def parse_record(e):
    r = json.loads(e)
    return r['ProductName'], r['Price']

p = df.Pipeline('DirectPipelineRunner')

(p
 | df.io.Read(df.io.TextFileSource('./datain*'))
 | df.Map(parse_record)
 | df.CombinePerKey(sum)
 | df.io.Write(df.io.TextFileSink('./dataout')))

p.run()
