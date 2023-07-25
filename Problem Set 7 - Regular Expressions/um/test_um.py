from um import count


def test_ome_um():
    assert count("um") == 1

def test_one_um_with_question_mark():
    assert count("um?") == 1

def test_um_sentence():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
