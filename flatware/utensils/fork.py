from flatware.utensils.spoon import make_spoon
from .spoon import make_spoon

from flatware.cup import make_cup
from ..cup import make_cup


class Fork( object ):
    def __repr__( self ):
        return "Fork()"
 
def make_fork():
    return Fork()


