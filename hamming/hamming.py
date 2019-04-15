def distance(strand_a: str, strand_b: str):
        if len(strand_a) != len(strand_b):
                raise ValueError("Strands not equal")

        distance: int = 0
        for i, el in enumerate(strand_a):
                if strand_b[i] != el:
                        distance += 1
        return distance
