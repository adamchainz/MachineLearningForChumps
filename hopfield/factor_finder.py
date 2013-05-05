# coding=utf-8
from storage import HopfieldStorageNet
from settler import HopfieldSettler

from utils import random_binary_array


class HopfieldFactorFinder(object):

    def __init__(self, num_nodes, num_samples, start=10, stop=30, step=1):
        self.num_nodes = num_nodes
        self.num_samples = num_samples

        # In percentages of num_nodes
        self.start = start
        self.stop = stop
        self.step = step

    def run(self):
        print "Running with {} nodes, trying from {}% to {}% memories and {} samples" \
              .format(self.num_nodes, self.start, self.stop, self.num_samples)

        results = {}
        for num in self.all_num_memories():
            results[num] = self.run_for(num)

        for num, percent_retrievable in results.iteritems():
            print "With {} memories ({:0.1f}%) - got {:0.1f}% retrieval" \
                  .format(
                      num,
                      self.get_percentage(num),
                      percent_retrievable
                  )

    def all_num_memories(self):
        last = -1
        all_nums = []
        for percentage in xrange(self.start, self.stop + 1, self.step):
            num = max(1, int((float(percentage)/100.0) * self.num_nodes))
            if num > last:
                all_nums.append(num)
                last = num

        return all_nums

    def get_percentage(self, num):
        return (100.0 * num) / self.num_nodes

    def run_for(self, num_memories):
        inspector = HopfieldFactorInspector(self.num_nodes,
                                            num_memories,
                                            num_samples=self.num_samples)
        return inspector.inspect()


class HopfieldFactorInspector(object):
    def __init__(self, num_nodes, num_memories, num_samples=5):
        self.num_nodes = num_nodes
        self.num_memories = num_memories
        # How many samples to draw as multiplier of num_memories
        self.num_samples = num_samples

    def inspect(self):
        num_successes = 0.0
        for i in xrange(self.num_samples):
            result = self.inspect_once()
            if result:
                num_successes += 1
        return (num_successes * 100.0) / self.num_samples

    def inspect_once(self):
        memories = self.generate_random_memories()
        net = HopfieldStorageNet(memories)

        num_hits = 0

        for memory in memories:
            net.set_nodes(memory)
            HopfieldSettler(net).settle()
            if (net.get_nodes() == memory).all():
                num_hits += 1

        return num_hits == self.num_memories

    def generate_random_memories(self):
        return [
            random_binary_array(self.num_nodes)
            for i in xrange(self.num_memories)
        ]

    def get_memory_index(self, memories, nodes):
        for i, memory in enumerate(memories):
            if (nodes == memory).all():
                return i
        return None


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-n',
                      '--num-nodes',
                      dest='num_nodes',
                      help='How many nodes to use in the hopfield network',
                      type='int',
                      default=20)
    parser.add_option('-s',
                      '--num-samples',
                      dest='num_samples',
                      help='How many times to sample each percentage',
                      type='int',
                      default=10)
    (options, args) = parser.parse_args()
    HopfieldFactorFinder(**options.__dict__).run()
