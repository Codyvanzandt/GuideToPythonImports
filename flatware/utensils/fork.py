from .spoon import make_spoon
from ..cup import make_cup

class Fork( object ):
    def __repr__( self ):
        return "Fork()"
 
def make_fork():
    return Fork()


