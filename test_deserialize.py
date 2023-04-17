#! /usr/bin/env python3
# Use flatbuffer compiler to generate (python) decoding code, for example online compiler 
# https://flatbuffers.ar.je
#
# Schema for classification, see
# https://github.com/SonySemiconductorSolutions/aitrios-sdk-vision-app-dev/tree/main/tutorials/4_prepare_application/1_develop/sample/schema
#
# Part of get_deserialize_data is from 
# https://github.com/SonySemiconductorSolutions/aitrios-sdk-cloud-app-sample-python
#
# Object detection decoding modules also from
# https://github.com/SonySemiconductorSolutions/aitrios-sdk-cloud-app-sample-python

from deserializer.get_deserialize_data import get_deserialize_data_od,  get_deserialize_data_classification
'''
encoded = 'DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAAAQAAABAAAAAMABQACAAHAAwAEAAMAAAAAAAAAQEAAAAUAAAAAADYPQwAEAAEAAAACAAMAAwAAAAMAAAAMwEAAFoAAAA='
decoded = get_deserialize_data_od(encoded)

print(f"INFERENCE DATA: {repr(encoded)}")
print(f"DESERIALIZED: {repr(decoded)}")
'''
encoded = 'DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAABQAAAEwAAAA0AAAAJAAAABQAAAAEAAAA0P///4sCAAAAAHA93P///18AAAAAAJg96P///5kDAAAAAPg99P///3MCAAAAAPg9CAAMAAQACAAIAAAAUQIAAAAA+D0='
decoded = get_deserialize_data_classification(encoded)

print(f"INFERENCE DATA: {repr(encoded)}")
print(f"DESERIALIZED: {repr(decoded)}")

print('Finished')
