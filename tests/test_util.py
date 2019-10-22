# -*- coding: utf-8 -*-
from nose.tools import eq_

from anytree.util import commonancestors, leftsibling, rightsibling
from anytree import Node


def test_commonancestors():
    """commonancestors."""
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    joe = Node("Joe", parent=dan)

    eq_(commonancestors(jet, joe), (udo, dan))
    eq_(commonancestors(jet, marc), (udo,))
    eq_(commonancestors(jet), (udo, dan))
    eq_(commonancestors(), ())
    eq_(commonancestors(jet, lian), (udo, ))


def test_leftsibling():
    """leftsibling."""
    dan = Node("Dan")
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    eq_(leftsibling(dan), None)
    eq_(leftsibling(jet), None)
    eq_(leftsibling(jan), jet)
    eq_(leftsibling(joe), jan)


def test_rightsibling():
    """rightsibling."""
    dan = Node("Dan")
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    eq_(rightsibling(dan), None)
    eq_(rightsibling(jet), jan)
    eq_(rightsibling(jan), joe)
    eq_(rightsibling(joe), None)
