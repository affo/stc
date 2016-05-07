'''
Every function gets an iterable that represents a trace.
    [ap1, ap2, ap3, ...]
'''

# TODO accept sequences with empty events

# TODO use izip with generators
# from itertools import izip

def ap (sym, trace, truth_f=None):
    if truth_f is None:
        truth_f = lambda ap: sym in ap

    return [truth_f(ap) for ap in trace]

def nnot (fi):
    return [not el for el in fi]

def oor (fi, psi):
    return [el1 or el2 for el1, el2 in zip(fi, psi)]

def implies (fi, psi):
    return oor(nnot(fi), psi)

def aand (fi, psi):
    return [el1 and el2 for el1, el2 in zip(fi, psi)]

# TODO cleanup, if possible
def until (fi, psi, interval):
    assert len(interval) == 2, '{}, should be an interval'.format(interval)
    assert interval[0] <= interval[1], 'The interval should be ordered'

    res = []

    for i in xrange(len(fi) - interval[0]):
        # considering the trace starting from i
        fi_trace = fi[i:]
        psi_trace = psi[i:]
        l = interval[0]
        h = min (interval[1] + 1, len(fi_trace))

        for j in xrange(l, h):
            if psi_trace[j]:
                # if exists j s.t. i <= j < len(trace)
                # and psi is true
                w_fi = fi_trace[1:j]

                if all(w_fi):
                    # fi holds in every k s.t.
                    # i < k < j
                    res.append(True)
                    break
        else:
            # a j s.t. blabla does not exist
            res.append(False)

    # fill res with false values where it couldn't be examined
    res.extend([False] * interval[0])

    return res

def eventually (fi, interval):
    return until([True] * len(fi), fi, interval)

def globally (fi, interval):
    return nnot(eventually(nnot(fi), interval))

def nnext (fi, interval):
    # nnext (fi, (0, N)) = nnext (fi, (1, N)) = nnext (fi, (1, 1))
    # nnext (fi, (>1, N)) = False
    if interval[0] == 0: interval[0] = 1
    if interval[1] < interval[0]: interval[1] = interval[0]
    return until([False] * len(fi), fi, interval)
