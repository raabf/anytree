from filecmp import cmp
from os import makedirs
from os.path import dirname
from os.path import exists
from os.path import join
from shutil import rmtree

from nose.tools import with_setup

from anytree import Node
from anytree.dotexport import RenderTreeGraph

TESTPATH = dirname(__file__)
GENPATH = join(TESTPATH, "dotexport")
REFPATH = join(TESTPATH, "refdata")


def setup():
    if not exists(GENPATH):
        makedirs(GENPATH)


def teardown():
    if exists(GENPATH):
        rmtree(GENPATH)


@with_setup(setup, teardown)
def test_tree1():
    """Tree1."""
    root = Node("root")
    s0 = Node("sub0", parent=root)
    Node("sub0B", parent=s0)
    Node("sub0A", parent=s0)
    s1 = Node("sub1", parent=root)
    Node("sub1A", parent=s1)
    Node("sub1B", parent=s1)
    s1c = Node("sub1C", parent=s1)
    Node(99, parent=s1c)

    RenderTreeGraph(root).to_dotfile(join(GENPATH, "tree1.dot"))
    assert cmp(join(GENPATH, "tree1.dot"), join(REFPATH, "tree1.dot"))


@with_setup(setup, teardown)
def test_tree2():
    """Tree2."""
    root = Node("root")
    s0 = Node("sub0", parent=root, edge=2)
    Node("sub0B", parent=s0, foo=4, edge=109)
    Node("sub0A", parent=s0, edge="")
    s1 = Node("sub1", parent=root, edge="")
    Node("sub1A", parent=s1, edge=7)
    Node("sub1B", parent=s1, edge=8)
    s1c = Node("sub1C", parent=s1, edge=22)
    Node("sub1Ca", parent=s1c, edge=42)

    def nodenamefunc(node):
        return '%s:%s' % (node.name, node.depth)

    def edgeattrfunc(node, child):
        return 'label="%s:%s"' % (node.name, child.name)
    r = RenderTreeGraph(root, options=["rankdir=LR;"],
                        nodenamefunc=nodenamefunc,
                        nodeattrfunc=lambda node: "shape=box",
                        edgeattrfunc=edgeattrfunc)

    r.to_dotfile(join(GENPATH, "tree2.dot"))
    assert cmp(join(GENPATH, "tree2.dot"), join(REFPATH, "tree2.dot"))


@with_setup(setup, teardown)
def test_tree_png():
    """Tree to png."""
    root = Node("root")
    s0 = Node("sub0", parent=root)
    Node("sub0B", parent=s0)
    Node("sub0A", parent=s0)
    s1 = Node("sub1", parent=root)
    Node("sub1A", parent=s1)
    Node("sub1B", parent=s1)
    s1c = Node("sub1C", parent=s1)
    Node("sub1Ca", parent=s1c)

    RenderTreeGraph(root).to_picture(join(GENPATH, "tree1.png"))
