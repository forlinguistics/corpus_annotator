import re
import prosodic as p


def meter_type(meter):
    iamb = re.compile('^(ws)*$')
    trochee = re.compile('^(sw)*$')
    anapest = re.compile('^(wws)*$')
    dactyl = re.compile('^(sww)*$')
    amphibrach = re.compile('^(wsw)*$')
    if bool(anapest.match(meter)):
        m_type = 'Anapest'
        n_feet = str(len(meter) / 3)
        return ((m_type, n_feet))
    if bool(amphibrach.match(meter)):
        m_type = 'Amphibrach'
        n_feet = str(len(meter) / 3)
        return ((m_type, n_feet))
    if bool(dactyl.match(meter)):
        m_type = 'Dactyl'
        n_feet = str(len(meter) / 3)
        return ((m_type, n_feet))
    if bool(iamb.match(meter)):
        m_type = 'Iamb'
        n_feet = str(len(meter) / 2)
        return ((m_type, n_feet))
    if bool(trochee.match(meter)):
        m_type = 'Trochee'
        n_feet = str(len(meter) / 2)
        return ((m_type, n_feet))
    return (("None", "None"))


def meters(line):
    p.config['print_to_screen'] = False
    final_jsons = []
    mline = line.replace('-', ' ')
    mline = p.Text(mline)
    mline.parse()
    i = mline.bestParses()
    final_json = {}
    if i != [] and i[0] is not None:

        meter = i[0].str_meter()
        final_json['meter'] = meter

        # final_json.clear()
    else:
        final_json['meter'] = '???'

    return final_json
