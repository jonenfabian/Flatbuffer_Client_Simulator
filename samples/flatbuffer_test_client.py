#!/usr/bin/python

import os
import sys
import struct
import time
if __name__ != '__main__':
    import Subfunctions.flatbuffers.python.flatbuffers
    import Subfunctions.flatbuffers.samples.MyButtons.Sample.Button
    import Subfunctions.flatbuffers.samples.MyButtons.Sample.Frame

def create_flatbuffer_from_temp_dict(temporary_dict):
    builder = flatbuffers.Builder(0)
    # Lets create the buttons with a loop
    button_vector=[]
    for button_label in temporary_dict:
        temp_priority = temporary_dict[button_label]["priority"]
        temp_rectangle = temporary_dict[button_label]["rectangle"]
        temp_color = temporary_dict[button_label]["color"]
        temp_button = builder.CreateString(button_label)
        MyButtons.Sample.Button.ButtonStart(builder)
        MyButtons.Sample.Button.ButtonAddX1(builder,temp_rectangle[0])
        MyButtons.Sample.Button.ButtonAddY1(builder,temp_rectangle[1])
        MyButtons.Sample.Button.ButtonAddX2(builder,temp_rectangle[2])
        MyButtons.Sample.Button.ButtonAddY2(builder,temp_rectangle[3])
        MyButtons.Sample.Button.ButtonAddColorR(builder,temp_color[0])
        MyButtons.Sample.Button.ButtonAddColorG(builder,temp_color[1])
        MyButtons.Sample.Button.ButtonAddColorB(builder,temp_color[2])
        MyButtons.Sample.Button.ButtonAddLabel(builder,temp_button)
        MyButtons.Sample.Button.ButtonAddPriority(builder, temp_priority)
        button_vector.append(MyButtons.Sample.Button.ButtonEnd(builder))

    MyButtons.Sample.Frame.FrameStartButtonsVector(builder, len(temporary_dict))
    # Note: Since we prepend the data, prepend the buttons in reverse order.
    for button_ in button_vector:
        builder.PrependUOffsetTRelative(button_)
    buttons = builder.EndVector()

    # Lets build the frame with all the buttons
    MyButtons.Sample.Frame.FrameStart(builder)
    MyButtons.Sample.Frame.FrameAddButtons(builder, buttons)
    frame = MyButtons.Sample.Frame.FrameEnd(builder)

    builder.Finish(frame)
    print("builded the buffer")
    return builder

def flatbuffer_gui_sender(rgb_frame,flatbuffer):
    # [0xAA, 0xAA, SIZE (4Byte), DATA(Flatbuffer) ]
    # result, rgb_frame = cv2.imencode('.jpg', rgb_frame, encode_param)
    # size = len(data)
    # my_bytes = bytearray()
    # my_bytes.append(123)
    # my_bytes.append(125)
    print("struct.pack(I, len(flatbuffer.Bytes)): ",struct.pack("I", len(flatbuffer.Bytes)))
    gui_client_socket.sendall(
        bytes([0xAA,0xAA]) # start Bytes
        + struct.pack("I", len(flatbuffer.Bytes)) # the 4-Byte array representing the size of the button dict
        + flatbuffer.Bytes)


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '../python'))
    import flatbuffers
    import MyButtons.Sample.Button
    import MyButtons.Sample.Frame
    import socket
    # set up the connection
    print("waiting for server")
    HOST="localhost"#"172.20.10.2"#"raspberrypi"#'10.0.1.230'#'172.20.10.2'#'192.168.0.19'#'localhost'
    PORT=8089
    gui_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # gui_client_socket.settimeout(3)
    gui_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    gui_client_socket.connect((HOST, PORT))
    print("connection established")

    #for testing lets create a temporary_dict as used in CAMERA_Process.py
    temporary_dict = {}
    delta = 20
    button_labels = ["Abort", "Exit", "Follow"]
    for i0 in range(len(button_labels)):
        # button_rectangle = [10,10+delta*i0,40,20+delta*i0]
        button_rectangle = [10,10+delta*i0,200,30+delta*i0]
        temporary_dict[button_labels[i0]] = {
            "rectangle" : button_rectangle,
            "on_click" : button_labels[i0],
            "priority" : 1, # if an object is behind a button,
                            # the button is prioritized in GUI process
            "color": [147,81,20], #RM signature
            }

    # Lets send stuff 100 times
    for x in range(100):
        builder = create_flatbuffer_from_temp_dict(temporary_dict)
        # We now have a FlatBuffer that we could store on disk or send over a network.
        #stream settings for GUI stream
        # ...Saving to file or sending over a network code goes here...
        flatbuffer_gui_sender(None,builder) #sending
        time.sleep(0.5)
    print("Done.")
