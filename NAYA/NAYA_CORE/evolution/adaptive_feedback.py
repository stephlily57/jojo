class AdaptiveFeedback:

    def learn(self, opportunity, result):

        if result.get("impact", 0) > 20000:
            print("Strategic refinement triggered")
