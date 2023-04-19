#! /usr/bin/env python
import base64
import json

import flatbuffers
from users.User import *

builder = flatbuffers.Builder(1024)
user_name = builder.CreateString("Arthur Dent")
Start(builder)  # Must come AFTER user_name...why?
AddName(builder, user_name)
AddId(builder, 42)
user = End(builder)
builder.Finish(user)

#buf = builder.Output()
#print(f"{buf}")

test = b"Hello World"
encoded = base64.b64encode(test)
decoded = base64.b64decode(encoded)
print(f"data: {test}, encoded: {encoded}. decoded: {decoded}")
assert(test == decoded)

"""
raw buf: b'\x0c\x00\x00\x00\x08\x00\x14\x00\x10\x00\x04\x00\x08\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x0b\x00\x00\x00Arthur Dent\x00'
base64 equivalent: b'DAAAAAgAFAAQAAQACAAAACoAAAAAAAAAAAAAAAQAAAALAAAAQXJ0aHVyIERlbnQA'
encoded = base64.b64encode(buf)
"""
encoded = b'DAAAAAgAFAAQAAQACAAAACoAAAAAAAAAAAAAAAQAAAALAAAAQXJ0aHVyIERlbnQA'
decoded = base64.b64decode(encoded)
print(f"encoded: {encoded}. decoded: {decoded}")
#assert(buf == decoded)

#user = User.GetRootAs(buf, 0)
user = User.GetRootAs(decoded, 0)
name = user.Name()
id = user.Id()
print(f"user:{name}, id:{id}")