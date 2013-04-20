# coding=utf-8
import numpy


class HopfieldNet(object):
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = numpy.zeros(num_nodes, dtype=numpy.int8)
        self.weights = numpy.zeros(num_nodes * num_nodes, dtype=numpy.int8)

    def get_node(self, which):
        return self.nodes[which - 1]

    def set_node(self, which, state):
        self.nodes[which - 1] = state

    def set_nodes(self, states):
        assert len(states) == self.num_nodes
        for i, state in enumerate(states, 1):
            self.set_node(i, state)

    def get_weight(self, i, j):
        if i > j:
            i, j = j, i

        i -= 1
        j -= 1

        return self.weights[j * self.num_nodes + i]

    def set_weight(self, i, j, weight):
        if i > j:
            i, j = j, i

        i -= 1
        j -= 1

        self.weights[j * self.num_nodes + i] = weight

    def get_node_bias(self, which):
        return 0

    def get_node_energy_gap(self, which):
        return (
            self.get_node_bias(which) +
            sum([
                self.get_node(other) * self.get_weight(which, other)
                for other in self._get_all_nodes_except(which)
                ])
        )

    def _get_all_nodes_except(self, which):
        for i in xrange(self.num_nodes):
            if i != which:
                yield i

    def get_total_energy(self):
        return -1 * sum(
            self.get_weight_state(i, j)
            for i, j in self.all_pairs()
        )

    def get_weight_state(self, i, j):
        return self.get_weight(i, j) * self.get_node(i) * self.get_node(j)

    def all_pairs(self):
        for i in xrange(1, self.num_nodes + 1):
            for j in xrange(1, i):
                yield (i, j)
