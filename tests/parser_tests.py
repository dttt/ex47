from nose.tools import *
from ex47 import parser


def test_peek():
    assert_equal(parser.peek([('direction', 'north')]), 'direction')
    assert_equal(parser.peek([('subject', 'I')]), 'subject')


def test_match():
    test_input_1 = ('direction', 'north')
    assert_equal(parser.match([test_input_1], 'direction'), test_input_1)


def test_skip():
    test_input = [
        ('stop', 'in'),
        ('direction', 'north'),
        ('noun', 'princess'),
    ]
    test_output = [
        ('direction', 'north'),
        ('noun', 'princess')
    ]
    parser.skip(test_input, 'stop')
    assert_equal(test_input, test_output)

    test_input_1 = [
        ('direction', 'south'),
        ('noun', 'prince'),
        ('verb', 'go')
    ]
    test_output_1 = [
        ('direction', 'south'),
        ('noun', 'prince'),
        ('verb', 'go')
    ]
    parser.skip(test_input_1, 'stop')
    assert_equal(test_input_1, test_output_1)


def test_parse_verb():
    verb_input = ('verb', 'go')
    assert_equal(
        parser.parse_verb([verb_input]),
        verb_input
        )

    not_verb_input = ('ver', 'princess')
    assert_raises(
        parser.ParserError,
        parser.parse_verb,
        [not_verb_input, verb_input]
        )
