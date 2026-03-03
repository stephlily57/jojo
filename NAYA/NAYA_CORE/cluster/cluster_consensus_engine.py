class ClusterConsensusEngine:

    def __init__(self, nodes):
        self.nodes = nodes

    def reach_consensus(self, proposal):
        votes = [node.vote(proposal) for node in self.nodes]
        return votes.count(True) > len(votes) // 2
