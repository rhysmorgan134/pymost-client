import serial

import struct
from threading import Timer, Thread

from serial.tools import list_ports


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class PiMost:

    def __init__(self, recv_most_message):
        self.port = None
        self.ser = None
        self.VID = 51966
        self.connected = False
        self.recv_most_message = recv_most_message
        self._connect_interval = RepeatedTimer(2, self.find_port)
        self.poll_pimost = Thread(target=self.poll)
        self.poll_pimost.setDaemon(True)
        self.poll_pimost.start()

        self._out_messages = {
            'force_switch': bytearray([0x55, 0x01, 0x74])
        }

    def force_switch(self):
        if self.connected:
            self.ser.write(self._out_messages['force_switch'])
        return

    def send_message(self):
        return

    def connect(self):
        self.ser = serial.Serial(port=self.port, baudrate=921600, bytesize=8, timeout=2)
        self.connected = True

    def find_port(self):
        device_list = list_ports.comports()
        print("finding port")
        for device in device_list:
            if device.vid is not None or device.pid is not None:
                if device.vid == self.VID:
                    self.port = device.device
                    self._connect_interval.stop()
                    self.connect()
                    print("found")
                    break

    def poll(self):
        while True:
            if self.connected:
                try:
                    # noinspection PyUnresolvedReferences
                    command = self.ser.read(3)
                    if len(command) > 0:
                        if command[0] == 85:
                            length = command[1]
                            type = command[2]
                            # noinspection PyUnresolvedReferences
                            message = self.ser.read(length)
                            if type == 0x01:
                                self.parse_message(message, length)
                except serial.serialutil.SerialException:
                    print("PiMost Disconnected")
                    self.connected = False
                    self.ser = None
                    self.port = None
                    self._connect_interval.start()

    def parse_message(self, data, length):
        raw_data = struct.unpack_from('>BBBBBHB', data, 0)
        message = data[8:len(data)]
        most_message = {
            'type': raw_data[0],
            'source_address_high': raw_data[1],
            'source_address_low': raw_data[2],
            'fBlock_id': raw_data[3],
            'instance_id': raw_data[4],
            'fkt_id': raw_data[5] >> 4,
            'op_type': raw_data[5] & 0xf,
            'tel_id': (raw_data[6] & 0xf) >> 4,
            'tel_len': raw_data[6] & 0xf,
            'data': message
        }
        self.recv_most_message(most_message)
