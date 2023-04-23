from french_exercises.core.model import f_decode_input


def test_decode_input():
    TXT = "Lorsque j'avais six ans j'ai vu, une fois, une <mask> image."
    TXT2 = (
        "J'ai montré mon chef-d'oeuvre aux grandes <mask> et je leur ai demandé si mon"
        " dessin leur faisait peur."
    )
    TXT3 = "je faisais l'expérience sur <mask> de mon dessin numéro Un"
    for txt in [TXT, TXT2, TXT3]:
        f_decode_input(txt)
    return
