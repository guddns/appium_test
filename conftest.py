import sys


def pytest_runtest_protocol(item, nextitem):
    doc = item.function.__doc__
    if doc is not None:
        try:
            # Try to encode the string as console's encoding (this may fail on some environments)
            # doc = doc.encode(sys.stdout.encoding).decode(sys.stdout.encoding)
            print("########### doc: " + doc)
        except UnicodeEncodeError:
            pass
    print("########### item.nodeid: " + str(item.nodeid))
    item._nodeid = item.nodeid + " 기본"
    return None
