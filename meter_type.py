import re
def meter_type (meter):
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
    return (("None","None"))