from vehicles.engines.truck_engine import TruckEngine

class Silverado( object ):

	def __init__( self ):
		self.engine = TruckEngine()

	def start( self ):
		return self.engine.start()
