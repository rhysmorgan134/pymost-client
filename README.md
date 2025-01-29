##  PiMost USB client

This is a basic client for the PiMost USB adapter. More functionality will be added, however currently it only supports force switching and receiving of MOST messages. For usage see the examples folder.

An example output

``` shell
finding port
found
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 0, 'source_address_high': 1, 'source_address_low': 134, 'fBlock_id': 34, 'instance_id': 5, 'fkt_id': 273, 'op_type': 12, 'tel_id': 0, 'tel_len': 1, 'data': b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 0, 'source_address_high': 1, 'source_address_low': 128, 'fBlock_id': 38, 'instance_id': 1, 'fkt_id': 259, 'op_type': 15, 'tel_id': 0, 'tel_len': 1, 'data': b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
most message received
{'type': 1, 'source_address_high': 1, 'source_address_low': 97, 'fBlock_id': 1, 'instance_id': 3, 'fkt_id': 0, 'op_type': 1, 'tel_id': 0, 'tel_len': 0, 'data': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}
```

when you supply a message received function, this will then get called from the class and a dictionary supplied with all the message details.
