# -*- coding: utf-8 -*-

import threading
import json
import time
import paho.mqtt.client as mqtt

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from display import Display


class CoreService(object):
    _comm_client = None
    _comm_delay = 0
    _thread_comms = None
    _thread_lock = None

    _thread_draw = None

    _status_channel_name = '/sensors/hud'
    _system_channel_name = '/system'

    _is_debug = False


    def __init__(self):
        pass

    def start(self):
        self._comm_client = mqtt.Client(
            client_id="service_hud",
            clean_session=True
        )

        self._comm_client.on_message = self._on_message
        self._comm_client.on_connect = self._on_connect
        self._comm_client.on_publish = self._on_publish
        self._comm_client.on_subscribe = self._on_subscribe

        self._thread_lock = threading.RLock()

        self._thread_comms = threading.Thread(target=self._start_thread_comms)
        self._thread_comms.setDaemon(True)
        self._thread_comms.start()

        self._display = Display()
        self._display.run()

        # self.output('{"sender": "service_hud", "message": "%s"}' % 1)

    def _on_connect(self, client, userdata, flags, rc):
        self.output('{"sender": "service_hud", "message": "Connected to GrandCentral."}')

        self._comm_client.subscribe('/sensors/temp', 0)

    def _on_message(self, client, userdata, msg):
        msg_struct = None

        try:
            msg_struct = json.loads(msg.payload)

        except:
            pass

        try:
            payload_obj = json.loads(msg.payload)
            self._display.lbl.text = str(payload_obj['temp']) + '°F'

        except:
            pass

    def _on_publish(self, mosq, obj, mid):
        pass

    def _on_subscribe(self, mosq, obj, mid, granted_qos):
        # msg = {
        #     'sender': 'service_hud',
        #     'message': 'Successfully subscribed to GrandCentral /system channel.'
        # }
        #
        # self.output(str(msg), self._system_channel_name)

        pass

    def _on_log(self, mosq, obj, level, string):
        pass

    def _connect_to_comms(self):
        comms_server = 'localhost'
        comms_port = 1883

        if self._is_debug:
            print('Connecting to comms system @ %s:%s' % (comms_server, comms_port))

        try:
            self._comm_client.connect(
                comms_server,
                comms_port,
                60
            )

        except Exception, e:
            if self._is_debug:
                print('Could not connect to local GrandCentral. Retry in one second.')

            time.sleep(1)
            self._connect_to_comms()

    def _start_thread_comms(self):
        if self._is_debug:
            print('Comms thread started.')

        self._thread_lock.acquire()

        try:
            self._connect_to_comms()

        finally:
            self._thread_lock.release()

        if self._is_debug:
            print('Connected to comms server.')

        while True:
            self._thread_lock.acquire()

            try:
                if self._comm_delay > 2000:
                    self._comm_client.loop()
                    self._comm_delay = 0

                else:
                    self._comm_delay += 1

            finally:
                self._thread_lock.release()

    def output(self, msg, channel=_status_channel_name):
        if self._comm_client:
            self._comm_client.publish(channel, msg)

        if self._is_debug:
            print(msg)
