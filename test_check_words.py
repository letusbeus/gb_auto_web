from soap_check_words import check_text


def test_check_words(good_word, bad_word):
    assert good_word in check_text(bad_word)
