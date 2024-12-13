import argparse, csv, glob, time, pprint, json
from grade import my_print as print
# import deepdiff

msg_ok  = '[OK]: \t  {points} point(s)\t {duration:.3f} ms\n'
msg_0points  = 'error: {points} points\t {duration:.3f} ms\n'
msg_err = 'error: {exname}\n\t{exmsg}\n'


class NotImplemented(Exception):
    pass


def rn(tests, verbose, logfile=''):
    results = []
    for test in tests:
        results.append(rnOne(test, verbose, logfile))
    return results


def rnOne(test, verbose, logfile='', stack_trace=False):
    try:
        doc=test.__doc__ or ''
        print(f'rnning {test.__name__}\t{doc}')
        start = time.time()
        v = test()
        end = time.time()
        if v:
            print(msg_ok.format(
                            points=v,
                            duration=(end-start)*1000))
        else:
            print(msg_0points.format(
                            points=v,
                            duration=(end-start)*1000))
    except NotImplemented:
        print("Not implemented: (None returned) ", test.__name__)
        v = 0
    except Exception as e:
        import traceback
        print(msg_err.format(
                             exname=e.__class__.__name__,
                             exmsg=str(e) if str(e) else ''))
        if stack_trace:
            print('*'*50+'[BEGIN STACK TRACE]'+'*'*50)
            traceback.print_exc()
            print('*'*50+'[END STACK TRACE]'+'*'*50)
        v = 0
    result = test.__name__, v
    log([result], logfile)
    return result


def description(tests):
    for test in tests:
        print(test.__name__ + ': ' + test.__help__)


def emptyLog(logfile):
    if logfile:
        with open(logfile,'w',newline='',encoding='utf8') as f:
            f.truncate()


def log(results, logfile):
    if logfile:
        with open(logfile, 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(results)

def checkDict(res, expected, params=None, expl=''):
    msg = ''
    if res == None:
        raise NotImplemented()
    keys_ex = set(expected.keys())
    keys_rez = set(res.keys())
    if params:
        msg += 'when input={}'.format(params)
    if res != expected:
        msg+='''\n[ERROR] I dizionari non sono uguali! Dictionaries differ!'''
        msg+=f'''\n[ERROR]  expected = {expected} returned = {res}'''
    if keys_ex == keys_rez:
        for k in expected:
            if expected[k] != res[k]:
                msg+=f'''\n[ERROR] Ad esempio, la chiave {k} dovrebbe avere il valore {expected[k]} invece che {res[k]}.'''
                msg+=f'''\n[ERROR] For example, key {k} should have a value of {expected[k]} instead of {res[k]}.'''
    else:
        diff_ex = keys_ex - keys_rez
        if diff_ex:
            msg+=f'''\n[ERROR] Al tuo dizionario mancano le chiavi {diff_ex}'''
            msg+=f'''\n[ERROR] Your dictionary misses the following key(s) {diff_ex}'''
        diff_rez = keys_rez - keys_ex
        if diff_rez:
            msg+=f'''\n[ERROR] Le seguenti chiavi {diff_rez} non dovrebbero esserci'''
            msg+=f'''\n[ERROR] The key(s) {diff_rez} should not be there'''
    assert res == expected, msg

def checkList(res, expected, params=None, expl=''):
    msg = ''
    if res == None:
        raise NotImplemented()
    if params:
        msg += 'when input={}'.format(params)
    if res != expected:
        msg+='''\n[ERROR] Le liste non sono uguali! Lists differ!'''
        msg+=f'''\n[ERROR]  expected = {expected} returned = {res}'''
        for i, p in enumerate(zip(res, expected)):
            x, y = p
            if x!=y:
                msg+=f'''\n[ERROR] Il primo elemento diverso è in posizione {i}'''
                msg+=f'''\n[ERROR] The first different element is item {i}'''
                msg+=f'''\n[ERROR] {y} != {x}, expected {expected[:i+1]}... returned {res[:i+1]}...'''
                break
        if len(res) > len(expected):
            msg+=f'''\n[ERROR] Le liste hanno lunghezza diversa! len(res)={len(res)} mentre len(expected)={len(expected)}'''
            msg+=f'''\n[ERROR] List lengths differ! len(res)={len(res)} but len(expected)={len(expected)}'''

    assert res == expected, msg

def checkString(res, expected, params=None, expl=''):
    msg = ''
    if res == None:
        raise NotImplemented()
    if params:
        msg += 'when input={}'.format(params)
    if res != expected:
        msg+='''\n[ERROR] Le stringe non sono uguali! Strings differ!'''
        msg+=f'''\n[ERROR]  expected = {expected} returned = {res}'''
        for i, p in enumerate(zip(res, expected)):
            x, y = p
            if x!=y:
                msg+=f'''\n[ERROR] Il primo elemento diverso è in posizione {i}'''
                msg+=f'''\n[ERROR] The first different element is item {i}'''
                msg+=f'''\n[ERROR] {y} != {x}, expected {expected[:i+1]}... returned {res[:i+1]}...'''
                break
        if len(res) > len(expected):
            msg+=f'''\n[ERROR] Le stringhe hanno lunghezza diversa! len(res)={len(res)} mentre len(expected)={len(expected)}'''
            msg+=f'''\n[ERROR] String lengths differ! len(res)={len(res)} but len(expected)={len(expected)}'''

    assert res == expected, msg

def check10(a, b, params=None, expl=''):
    msg = ''
    if params:
        msg += '\twhen input={}'.format(params)
    msg += '\n\t\t%r != %r' % (a, b)
    if expl:
        msg += "\t<- correct %s value" % expl
    assert a == b,  msg


def check(a, b, params=None, expl='', other=None):
    msg = ''
    if params:
        msg += 'when input={}'.format(params)
    if other:
        msg += '\n\t\t%r != %r ' % (other[0], other[1])
    else:
        msg += '\n\t%r \n\t!= \n\t%r\n\n' % (a, b)
    if expl:
        msg += "\t<-  %s\n\n\n" % expl
    if (a == None) | (a == type(None)):
        raise NotImplemented()
    # if a != b:
    #     pprint.pprint(deepdiff.DeepDiff(a, b))
    assert a == b,  msg


def check1(a, b, params=None, expl='', other=None):
    msg = ''
    if params:
        msg += 'when input={}'.format(params)
    if other:
        msg += '\n\t\t%r != %r ' % (other[0], other[1])
    else:
        msg += '\n\t%r \n\t!= \n\t%r\n\n' % (a, b)
    if expl:
        msg += "\t<-  %s\n\n\n" % expl
    if a == None:
        raise NotImplemented()
    assert a == b,  msg


def check_text_file(a,b):
    with open(a, 'r', encoding='utf8') as f: txt_a = f.read()
    with open(b, 'r', encoding='utf8') as f: txt_b = f.read()
    lines_a = [l.strip() for l in txt_a.splitlines()]
    lines_b = [l.strip() for l in txt_b.splitlines()]
    for ln, p in enumerate(zip(lines_a, lines_b)):
        la, lb = p
        if la != lb:
            for cn, p in enumerate(zip(la, lb)):
                x, y = p
                assert x==y, f'text differ at line {ln+1}, char {cn+1}:' + x + '!=' + y

    # assert lines_a == lines_b, 'text differ: ' + a + ' ' + b


def check_json_file(a,b, params=None, expl='', other=''):
    with open(a, 'r', encoding='utf8') as f: da = json.load(f)
    with open(b,' r', encoding='utf8') as f: db = json.load(f)
    check(da, db, params, expl, other)


def image_load(filename):
    '''Load the PNG image from the PNG file under 'filename',
       convert it into tuple-matrix format and return it'''
    import png
    with open(filename, 'rb') as f:
        # Read the image as an RGB-file with 256 colours (without transparency)
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        # Convert the list of lists into tuples. Notice that the PNG colours
        # are triples in the png_img array, so we read them by a step of three.
        w *= 3
        return [[(line[i], line[i + 1], line[i + 2])
                 for i in range(0, w, 3)]
                for line in png_img]
    return img


def check_img_file(a, b):
    img_a = image_load(a)
    img_b = image_load(b)
    ha = len(img_a)
    hb = len(img_b)
    assert ha == hb, 'Images have different heights: {} != {}'.format(ha, hb)
    assert ha > 0 and hb > 0, 'An image has a height of 0: {} {}'.format(ha, hb)
    wa = len(img_a[0])
    wb = len(img_b[0])
    assert wa == wb, 'Images have different widths: {} != {}'.format(wa, wb)
    assert wa > 0 and wb > 0, 'An image has a height of 0: {} {}'.format(wa, wb)
    for y in range(ha):
        for x in range(wa):
            ca = img_a[y][x]
            cb = img_b[y][x]
            assert ca == cb, \
                   'Images differ at coordinates {},{} : {} != {}'.format(
                       x, y, ca, cb)


def rntests(tests, verbose=True, logfile='', stack_trace=False):
    if logfile:
        emptyLog(logfile)
        for test in tests:
            rnOne(test, verbose, logfile, stack_trace)
        with open(logfile, newline='', encoding='utf8') as f:
            tot = 0
            reader = csv.reader(f)
            for row in reader:
                tot += float(row[1])
        print('Total score:', tot)
    else:
        for test in tests:
            rnOne(test, verbose, logfile, stack_trace)


import tempfile, os, os.path


class randomized_filename:

    def __init__(self, filename):
        name, ext = filename.split('.')
        self.filename = filename
        self.randomized = next(tempfile._get_candidate_names()) + '.' + ext

    def __enter__(self):
        if os.path.isfile(self.filename):
            print(self.filename, ' -> ', self.randomized)
            os.rename(self.filename, self.randomized)
        return self.randomized

    def __exit__(self, type, value, traceback):
        if os.path.isfile(self.randomized):
            print(self.filename, ' <- ', self.randomized)
            os.rename(self.randomized, self.filename)

