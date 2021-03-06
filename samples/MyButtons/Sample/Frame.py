# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample

import flatbuffers

class Frame(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFrame(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Frame()
        x.Init(buf, n + offset)
        return x

    # Frame
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Frame
    def Buttons(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Button import Button
            obj = Button()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Frame
    def ButtonsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def FrameStart(builder): builder.StartObject(1)
def FrameAddButtons(builder, buttons): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(buttons), 0)
def FrameStartButtonsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FrameEnd(builder): return builder.EndObject()
