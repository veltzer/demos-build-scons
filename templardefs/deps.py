'''
dependencies for this project
'''

def populate(d):
    d.packs=[
        # for scons(1)
        'scons',
        # for scons docs
        'scons-doc',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
