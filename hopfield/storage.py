# coding=utf-8
from net import HopfieldNet
from utils import string_to_binary_array


class HopfieldStorageNet(HopfieldNet):

    def __init__(self, memories):
        length = len(memories[0])
        assert len([x for x in memories if len(x) != length]) == 0

        super(HopfieldStorageNet, self).__init__(length)

        for memory in memories:
            self.store(memory)

    def store(self, memory):
        for i, j in self.all_pairs():
            weight = self.get_weight(i, j)
            weight += (
                4 *
                (memory[i] - 0.5) *
                (memory[j] - 0.5)
            )
            self.set_weight(i, j, weight)


class HopfieldStringStorageNet(HopfieldStorageNet):
    def __init__(self, strings):
        memories = [
            string_to_binary_array(string)
            for string in strings
        ]
        super(HopfieldStringStorageNet, self).__init__(memories)

