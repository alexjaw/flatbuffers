import base64
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

def get_deserialize_data_classification(serialize_data):
    """Get access information from yaml and generate ConsoleAccess client
    Returns:
        ConsoleAccessClient: CosoleAccessClient Class generated from access information.
    """
    buf = {}
    buf_decode = base64.b64decode(serialize_data)
    ppl_out = ClassificationTop.ClassificationTop.GetRootAsClassificationTop(buf_decode, 0)
    obj_data = ppl_out.Perception()
    res_num = obj_data.ClassificationListLength()
    for i in range(res_num):
        obj_list = obj_data.ClassificationList(i)
        buf[str(i + 1)] = {}
        buf[str(i + 1)]['C'] = obj_list.ClassId()
        buf[str(i + 1)]['P'] = obj_list.Score()

    return buf
