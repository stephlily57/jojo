class SpecializationVotingManager:
    def __init__(self):
        self.votings = {}
        self.consensus_threshold = 0.6  # Example threshold for consensus

    def start_voting(self, specialization):
        if specialization not in self.votings:
            self.votings[specialization] = {'votes': [], 'confidence': 0}
            print(f'Started voting for specialization: {specialization}')
        else:
            print(f'Voting for specialization {specialization} already in progress.')

    def cast_vote(self, specialization, vote):
        if specialization in self.votings:
            self.votings[specialization]['votes'].append(vote)
            print(f'Vote cast for {specialization}: {vote}')
            self.update_confidence(specialization)
        else:
            print(f'No voting in progress for specialization: {specialization}')

    def update_confidence(self, specialization):
        total_votes = len(self.votings[specialization]['votes'])
        if total_votes > 0:
            positive_votes = sum(1 for vote in self.votings[specialization]['votes'] if vote)
            confidence = positive_votes / total_votes
            self.votings[specialization]['confidence'] = confidence
            print(f'Updated confidence for {specialization}: {confidence}')
            if confidence >= self.consensus_threshold:
                print(f'Consensus reached for {specialization}.')
        else:
            print(f'No votes to calculate confidence for {specialization}.')

    def get_voting_info(self, specialization):
        return self.votings.get(specialization, 'No voting in progress for this specialization.')

# Example usage
if __name__ == '__main__':
    manager = SpecializationVotingManager()
    manager.start_voting('AI Development')
    manager.cast_vote('AI Development', True)
    manager.cast_vote('AI Development', False)
    manager.cast_vote('AI Development', True)
    print(manager.get_voting_info('AI Development'))
