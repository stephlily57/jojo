import concurrent.futures

class LLMOrchestrator:

    def __init__(self, providers, doctrine):
        self.providers = providers
        self.doctrine = doctrine

    def run_parallel(self, prompt):

        results = {}

        def call(provider):
            return provider.generate(prompt)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_map = {
                executor.submit(call, p): p.name
                for p in self.providers
            }

            for future in concurrent.futures.as_completed(future_map):
                provider_name = future_map[future]
                try:
                    results[provider_name] = future.result()
                except:
                    results[provider_name] = None

        return self.vote(results)

    def vote(self, results):
        # Simplifié — à enrichir avec Doctrine réelle
        valid = [r for r in results.values() if r]
        if not valid:
            return None
        return self.doctrine.select_best(valid)
