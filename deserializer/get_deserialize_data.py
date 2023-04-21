"""
decode base64 + fb deserialization time:  0.25..0.53 ms
corresponding time for c++             :  0.006..0.008 ms (-O3 optimization)

Test result:
INFERENCE DATA: 'DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAABQAAAEwAAAA0AAAAJAAAABQAAAAEAAAA0P///4sCAAAAAHA93P///18AAAAAAJg96P///5kDAAAAAPg99P///3MCAAAAAPg9CAAMAAQACAAIAAAAUQIAAAAA+D0='
DESERIALIZED: {'1': {'C': 593, 'P': 0.12109375}, '2': {'C': 627, 'P': 0.12109375}, '3': {'C': 921, 'P': 0.12109375}, '4': {'C': 95, 'P': 0.07421875}, '5': {'C': 651, 'P': 0.05859375}}
"""
import base64
from time import perf_counter
from decode_python import ClassificationTop


def get_deserialize_data_od(serialize_data):
    """Get access information from yaml and generate ConsoleAccess client
    Returns:
        ConsoleAccessClient: CosoleAccessClient Class generated from access information.
    """
    buf = {}
    """
    buf_decode = base64.b64decode(serialize_data)
    ppl_out = object_detection_top.ObjectDetectionTop.GetRootAsObjectDetectionTop(buf_decode, 0)
    obj_data = ppl_out.Perception()
    res_num = obj_data.ObjectDetectionListLength()
    for i in range(res_num):
        obj_list = obj_data.ObjectDetectionList(i)
        union_type = obj_list.BoundingBoxType()
        if union_type == bounding_box.BoundingBox.BoundingBox2d:
            bbox_2d = bounding_box_2d.BoundingBox2d()
            bbox_2d.Init(obj_list.BoundingBox().Bytes, obj_list.BoundingBox().Pos)
            buf[str(i + 1)] = {}
            buf[str(i + 1)]['C'] = obj_list.ClassId()
            buf[str(i + 1)]['P'] = obj_list.Score()
            buf[str(i + 1)]['X'] = bbox_2d.Left()
            buf[str(i + 1)]['Y'] = bbox_2d.Top()
            buf[str(i + 1)]['x'] = bbox_2d.Right()
            buf[str(i + 1)]['y'] = bbox_2d.Bottom()
    """
    return buf

def get_deserialize_data_classification_new(serialize_data):
    """ See https://flatbuffers.dev/flatbuffers_guide_tutorial.html
    Python
    """
    #print("--- get_deserialize_data_classification_new()")
    tic = perf_counter()
    buf_decode = base64.b64decode(serialize_data)
    detections = ClassificationTop.ClassificationTop.GetRootAs(buf_decode, 0)
    perception = detections.Perception()
    toc = perf_counter()
    print(f"decode base64 + fb deserialization time: {(toc - tic)*1000} ms")
    #print(dir(perception))
    #print(dir(perception.ClassificationList(0)))
    buf = {}
    for i in range(perception.ClassificationListLength()):
        classification = perception.ClassificationList(i)
        #print(f"{i}. C:{classification.ClassId()}, P:{classification.Score()}")
    #print("--- get_deserialize_data_classification_new()")
    return buf

def get_deserialize_data_classification(serialize_data):
    """Get access information from yaml and generate ConsoleAccess client
    Returns:
        ConsoleAccessClient: CosoleAccessClient Class generated from access information.
    """
    get_deserialize_data_classification_new(serialize_data)
    buf_decode = base64.b64decode(serialize_data)
    ppl_out = ClassificationTop.ClassificationTop.GetRootAsClassificationTop(buf_decode, 0)
    obj_data = ppl_out.Perception()
    res_num = obj_data.ClassificationListLength()
    buf = {}
    for i in range(res_num):
        obj_list = obj_data.ClassificationList(i)
        buf[str(i + 1)] = {}
        buf[str(i + 1)]['C'] = obj_list.ClassId()
        buf[str(i + 1)]['P'] = obj_list.Score()

    return buf
