modes = {
         'aar': ['Latn'],
         'amh': ['Ethi-pp', 'Ethi-red', 'Ethi'],
         'ara': ['Arab'],
         'aze': ['Latn', 'Cyrl'],
         'ben': ['Beng', 'Beng-red'],
         'cat': ['Latn'],
         'ceb': ['Latn'],
         'ces': ['Latn'],
         'ckb': ['Arab'],
         'deu': ['Latn', 'Latn-np'],
         'fas': ['Arab'],
         'fra': ['Latn', 'Latn-np'],
         'hat': ['Latn-bab'],
         'hau': ['Latn'],
         'hin': ['Deva'],
         'hun': ['Latn'],
         'ilo': ['Latn'],
         'ind': ['Latn'],
         'ita': ['Latn'],
         'jav': ['Latn'],
         'kaz': ['Cyrl', 'Cyrl-bab', 'Latn'],
         'khm': ['Khmr'],
         'kin': ['Latn'],
         'kir': ['Cyrl', 'Arab', 'Latn'],
         'kmr': ['Latn', 'Latn-red'],
         'lao': ['Laoo'],
         'mar': ['Deva'],
         'mlt': ['Latn'],
         'mon': ['Cyrl-bab'],
         'msa': ['Latn'],
         'mya': ['Mymr'],
         'nld': ['Latn'],
         'nya': ['Latn'],
         'orm': ['Latn'],
         'pan': ['Guru'],
         'pol': ['Latn'],
         'por': ['Latn'],
         'ron': ['Latn'],
         'rus': ['Cyrl'],
         'sag': ['Latn'],
         'sna': ['Latn'],
         'som': ['Latn'],
         'spa': ['Latn'],
         'swa': ['Latn', 'Latn-red'],
         'swe': ['Latn'],
         'tam': ['Taml', 'Taml-red'],
         'tel': ['Telu'],
         'tgk': ['Cyrl'],
         'tgl': ['Latn', 'Latn-red'],
         'tha': ['Thai'],
         'tir': ['Ethi-pp', 'Ethi-red', 'Ethi'],
         'tuk': ['Latn', 'Cyrl'],
         'tur': ['Latn', 'Latn-bab', 'Latn-red'],
         'uig': ['Arab'],
         'ukr': ['Cyrl'],
         'urd': ['Arab'],
         'uzb': ['Latn', 'Cyrl'],
         'vie': ['Latn'],
         'xho': ['Latn'],
         'yor': ['Latn'],
         'zha': ['Latn'],
         'zul': ['Latn']
         }


def supported_lang(iso639):
    return iso639 in modes


def get_default_mode(iso639):
    try:
        return '-'.join([iso639, modes[iso639][0]])
    except KeyError:
        return None