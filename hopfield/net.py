# coding=utf-8
import numpy


class HopfieldNet(object):
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = numpy.zeros(num_nodes, dtype=numpy.int8)
        self.biases = numpy.zeros(num_nodes, dtype=numpy.int8)
        self.weights = numpy.zeros(num_nodes * num_nodes, dtype=numpy.int8)

    def set_node(self, which, state):
        self.nodes[which] = state

    def set_nodes(self, states):
        assert len(states) == self.num_nodes
        for i, state in enumerate(states):
            self.nodes[i] = state

    def get_nodes(self):
        return self.nodes

    def get_node_bias(self, which):
        return self.biases[which]

    def set_node_bias(self, which, bias):
        self.biases[which] = bias

    def get_weight(self, i, j):
        if i > j:
            i, j = j, i

        return self.weights[j * self.num_nodes + i]

    def set_weight(self, i, j, weight):
        if i > j:
            i, j = j, i

        self.weights[j * self.num_nodes + i] = weight

    def get_node_energy_gap(self, which):
        return (
            self.biases[which] +
            sum([
                self.nodes[other] * self.get_weight(which, other)
                for other in xrange(self.num_nodes)
                if other != which
                ])
        )

    def get_total_energy(self):
        return -1 * sum(
            self.get_weight_state(i, j)
            for i, j in self.all_pairs()
        )

    def get_weight_state(self, i, j):
        if i > j:
            i, j = j, i
        return self.weights[j * self.num_nodes + i] * self.nodes[i] * self.nodes[j]

    def all_pairs(self):
        for i in xrange(self.num_nodes):
            for j in xrange(i):
                yield (i, j)
