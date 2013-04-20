# coding=utf-8
import random


class HopfieldTrainer(object):
    def __init__(self, net):
        self.net = net

    def settle(self):
        while True:
            self.do_a_round()

            if self.at_energy_minimum():
                break

    def do_a_round(self):
        energy_streak = 0
        previous_energy = self.net.get_total_energy()

        while True:
            current_energy = self.net.get_total_energy()

            if current_energy == previous_energy:
                energy_streak += 1
            else:
                energy_streak = 0

            if energy_streak >= 5:
                break

            previous_energy = current_energy

            self.update_random_node()

    def update_random_node(self):
        which = random.randint(1, self.net.num_nodes)
        self.update_node(which)

    def update_node(self, which):
        energy_gap = self.net.get_node_energy_gap(which)

        if energy_gap < 0:
            return self.net.set_node(which, False)
        elif energy_gap > 0:
            return self.net.set_node(which, True)
        else:
            return False

    def at_energy_minimum(self):
        """
        To determine if we are at a minimum from where we are, we should try to
        update each node once - if we can update it, it means we aren't, so we
        should continue updating randomly.

        NB could be fairer by iterating across all nodes randomly.
        """
        for i in xrange(self.net.num_nodes):
            if self.update_node(i):
                return False

        return True
