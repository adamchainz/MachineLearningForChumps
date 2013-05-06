# coding=utf-8
import random


class HopfieldSettler(object):
    def __init__(self, net):
        self.net = net

    def settle(self):
        while True:
            updated = self.maybe_update()
            if not updated:
                break

    def maybe_update(self):
        """
        Loop over all nodes in a random order - find the first updatable one
        and update it and return True. If there are no updatable nodes,
        return False.
        """
        all_nodes = range(self.net.num_nodes)
        random.shuffle(all_nodes)
        for node in all_nodes:
            if self.could_update_node(node):
                self.net.nodes[node] = (self.net.nodes[node] + 1) % 2
                return True
        return False

    def could_update_node(self, which):
        return self.get_node_desired_state(which) != self.net.nodes[which]

    def get_node_desired_state(self, which):
        energy_gap = self.net.get_node_energy_gap(which)
        if energy_gap < 0:
            return False
        else:
            return True
