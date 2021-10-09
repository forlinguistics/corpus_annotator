from poesy import Poem


def rhyme_scheme(text):
    poem = Poem(text)
    rhyme_sch = poem.rhymed
    if rhyme_sch['rhyme_scheme_accuracy'] >= 0.4:
        return (True, rhyme_sch['rhyme_scheme'])
    else:
        return (False,'None')


