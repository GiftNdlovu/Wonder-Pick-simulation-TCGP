import random

def simulate_wonder_picks(num_simulations=1000):
    wonder_picks = ["Pikachu", "Weezing", "Snivy", "Tepig", "Pikachu EX"]
    pikachu_ex_counts = [0] * len(wonder_picks)

    print("Simulation Start:")
    print("-" * 40)

    for sim in range(1, num_simulations + 1):
        # Randomize the pool before the round
        before_shuffle = wonder_picks[:]
        random.shuffle(wonder_picks)
        after_shuffle = wonder_picks[:]

        # Find and track the position of Pikachu EX
        for idx, card in enumerate(after_shuffle):
            if card == "Pikachu EX":
                pikachu_ex_counts[idx] += 1

        # Print results for the round
        print(f"Round {sim}:")
        print(f"  Before: {before_shuffle}")
        print(f"  After:  {after_shuffle}")
        print()

    print("-" * 40)
    print("Simulation Summary:")
    for idx, count in enumerate(pikachu_ex_counts, start=1):
        print(f"Position {idx}: Pikachu EX appeared {count} times.")
    print("-" * 40)

# Run the simulation
simulate_wonder_picks(1000)
