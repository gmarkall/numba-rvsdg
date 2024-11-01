# numba-rvsdg and Numba frontend

THis repository contains numba-rvsdg and a Numba frontend for experimentation
with the IR forms produced by numba-rvsdg.

## Setup

Create an environment with:

```
mamba create -n numba-rvsdg-experiments python=3.11 python-graphviz pyyaml \
                                        ipython jupyter numba
```

Activate the environment:

```
conda activate numba-rvsdg-experiments
```

Install numba-rvsdg as an editable install (to facilitate experiments by
changing the code in the repo, if wanted / needed):

```
pip install -e .
```

## Examples

Examples are in the [`examples/`](examples) folder. A notebook with the examples
and the code to render the different forms of the representation can be executed
as:

```
jupyter notebook examples/Examples.ipynb
```

The renderings produced by the notebook are also saved in the
[`example1`](examples/example1) [`example2`](examples/example2)
[`example3`](examples/example3) subfolders.

## Original README

See [README.original.md](README.original.md)
