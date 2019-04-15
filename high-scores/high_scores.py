class HighScores:

    def __init__(self, scores:[int]):
        self.scores = scores
        self.sorted_scores = sorted(scores, reverse=True)

    def latest(self) -> int:
        return self.scores[-1]

    def personal_best(self)->int:
        return max(self.scores)

    def personal_top_three(self)->[int]:
        return self.sorted_scores[:3]