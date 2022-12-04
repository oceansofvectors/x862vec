class Normalizer:
    def __init__(self):
        pass

    def normalize_assembly(self, assembly) -> list:
        lines = assembly.split('\n')
        normalized_lines = list()
        for line in lines:
            if "#" in line:
                line = line.split("#")[0]
            word = line.strip().split("   ")
            if len(word) > 1:
                word = f"{word[-2]} {word[-1]}".strip()
                normalized_lines.append(word)
        print(len(normalized_lines))
        return normalized_lines
