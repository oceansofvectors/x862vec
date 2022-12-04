import os

from elftools.common.exceptions import ELFError
from tqdm import tqdm

from src.preprocess.binary import Binary
from src.preprocess.normalizer import Normalizer


class Corpus:
    def __init__(self, max_binaries):
        self.normalizer = Normalizer()
        self.max_binaries = max_binaries
        self.corpus_file = open("assets/corpus", "w")

    def build_corpus(self):
        binaries = os.listdir('/usr/bin')
        try:
            binaries.remove('gtk4-encode-symbolic-svg')
            binaries.remove('shotwell')
            binaries.remove('fish_key_reader')
            binaries.remove('perl5.34.0')
            binaries.remove('bash')
            binaries.remove('perl')
            binaries.remove('evince')
            binaries.remove('isovfy')
            binaries.remove('speech-dispatcher')
            binaries.remove('gnome-todo')
            binaries.remove('Xephyr')
            binaries.remove('fwupdtool')
            binaries.remove('rbash')
            binaries.remove('remmina')
            binaries.remove('gcalccmd')
            binaries.remove('gnome-calendar')
            binaries.remove('brltty-ctb')
            binaries.remove('mkisofs')
            binaries.remove('brltty-trtxt')
            binaries.remove('lto-dump-11')
            binaries.remove('python3')
            binaries.remove('gnome-control-center')
            binaries.remove('fish')
            binaries.remove('x86_64-linux-gnu-lto-dump-11')
            binaries.remove('pptpsetup')
        except Exception:
            pass
        binaries = list(set(binaries))
        for binary in tqdm(binaries[0:self.max_binaries]):
            if os.path.isdir(f"/usr/bin/{binary}"):
                continue
            print(f"Processing: {binary}")
            try:
                b = Binary(filepath=f"/usr/bin/{binary}")
                if b.size() > 536792:
                    continue
                assembly = b.assembly()
                assembly_lines = self.normalizer.normalize_assembly(assembly)
                for line in assembly_lines:
                    self.corpus_file.write(f"{line}\n")
            except ELFError:
                pass

        self.corpus_file.close()
