def cdf2histogram(c_in):
    """ Reads cdf as list and returns histogram. """
    h = []
    h.append(c_in[0])
    for i in range(1, len(c_in)):
        h.append(c_in[i] - c_in[i-1])
    return h


def dict2file(d, nameoffile='dict.txt', sorted=True):
    """ Writes dictionary (or list or tuple) to a textfile
        Sorted by keys, if sorted=True.
    """
    def list2dict(li):
        x = {}
        for (i, el) in enumerate(li):
            x[i] = el
        return x

    if not isinstance(d, dict):
        d = list2dict(d)

    dk = d.keys()
    if sorted:
        dk.sort()

    # if d={ 1: [a,b,c,...], 2:[d,e,f,...],... }
    s = d.values()[0]
    if isinstance(s, dict) or isinstance(s, list) or isinstance(s, tuple):
        laenge = len(d.values()[0])
        g = file(nameoffile, 'w+')
        for k in dk:
            wstring = ''
            for l in range(laenge):
                wstring += '\t' + str(d[k][l])
            g.writelines((str(k) + wstring + '\n'))
        g.close
        return

    g = file(nameoffile, 'w+')
    for k in dk:
        g.writelines((str(k), '\t', str(d[k]), '\n'))
    g.close

    return
