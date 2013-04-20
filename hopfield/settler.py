# coding=utf-8
import random


class HopfieldSettler(object):
    def __init__(self, net):
        self.net = net

    def settle(self):
        while True:
            self.do_a_round()

            if self.at_energy_minimum():
                break

    def do_a_round(self):
        """
        Because we are updating probabilistically, we must guess that we are
        near a minimum by recording a streak of non-movement in energy.
        """
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
        which = random.randint(0, self.net.num_nodes - 1)
        state = self.get_node_desired_state(which)
        self.net.set_node(which, state)

    def at_energy_minimum(self):
        """
        We are at the minimum if updating any single node would only make the
        energy higher - although it may be a local as opposed to global
        minimum.
        """
        for i in xrange(self.net.num_nodes):
            if self.could_update_node(i):
                return False

        return True

    def could_update_node(self, which):
        return self.get_node_desired_state(which) != self.net.get_node(which)

    def get_node_desired_state(self, which):
        energy_gap = self.net.get_node_energy_gap(which)
        if energy_gap < 0:
            return False
        else:
            return True
