name = "tweener"

version = "1.0.10"

authors = [
    "monoteba",
    "Jeremy Andriambolisoa",
]

description = \
    """
    Tweener is a tool similar to TweenMachine or aTools/animBot.
    It allows you to quickly create in-betweens or adjust existing keys
    by interpolating towards adjacent keyframes, and can speed-up
    your workflow when creating breakdowns and in-betweens.
    """

requires = [
    "python-3+",
    "maya-2025+"
]

uuid = "monoteba.tweener"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")