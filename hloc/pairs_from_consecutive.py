from pathlib import Path
from typing import Optional, Union, List

def main(
        output: Path,
        image_list: Optional[Union[Path, List[str]]] = None):
    names_q = list(image_list)
    pairs = []
    for i in range(len(names_q)-1):
        pairs.append((names_q[i], names_q[i+1]))
    with open(output, 'w') as f:
        f.write('\n'.join(' '.join([i, j]) for i, j in pairs))
