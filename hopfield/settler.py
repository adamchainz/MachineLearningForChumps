# coding=utf-8
import random


class HopfieldSettler(object):
    def __init__(self, net):
        self.net = net

    def settle(self):
        while True:
            updatable = self.find_updatable()

            if len(updatable) == 0:
                return
            else:
                self.update_one_of(updatable)

    def find_updatable(self):
        updatable = []
        for which in xrange(self.net.num_nodes):
            if self.could_update_node(which):
                updatable.append(which)
        return updatable

    def update_one_of(self, updatable):
        i = random.randint(0, len(updatable) - 1)
        which = updatable[i]
        state = self.get_node_desired_state(which)
        self.net.set_node(which, state)

    def could_update_node(self, which):
        return self.get_node_desired_state(which) != self.net.get_node(which)

    def get_node_desired_state(self, which):
        energy_gap = self.net.get_node_energy_gap(which)
        if energy_gap < 0:
            return False
        else:
            return True
