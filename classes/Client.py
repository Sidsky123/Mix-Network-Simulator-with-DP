import numpy as np
import copy
import sys
import random

from classes.Packet import Packet
from classes.Message import Message
from classes.Node import Node
from classes.Utilities import StructuredMessage, setup_logger, random_string
import experiments.Settings


class Client(Node):
    def __init__(self, env, conf, net, loggers=None, label=0, id=None, p2p=False):
        self.conf = conf
        super().__init__(env=env, conf=conf, net=net, loggers=loggers, id=id)

    # def generate_gaussian_noise(epsilon, delta):
    #     sigma = np.sqrt(2 * np.log(1.25 / delta)) * (1 / epsilon)
    #     noise = np.random.normal(0, sigma)
    #     return noise

    # def start_loop_cover_traffic(self, epsilon, delta, sensitivity):
    #     # Client-specific pre-processing or checks
    #     print("Client-specific traffic handling starting.")

    #     # Call the parent class method using super()
    #     super().start_loop_cover_traffic()

    #     # Client-specific post-processing
    #     print("Client-specific traffic handling completed.")

    def schedule_retransmits(self):
        pass

    def schedule_message(self, message):
        #  This function is used in the transcript mode
        ''' schedule_message adds given message into the outgoing client's buffer. Before adding the message
            to the buffer the function records the time at which the message was queued.'''

        print("> Scheduled message")
        current_time = self.env.now
        message.time_queued = current_time
        for pkt in message.pkts:
            pkt.time_queued = current_time
        self.add_to_buffer(message.pkts)


    def print_msgs(self):
        ''' Method prints all the messages gathered in the buffer of incoming messages.'''
        for msg in self.msg_buffer_in:
            msg.output()
