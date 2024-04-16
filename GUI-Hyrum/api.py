from cinp.client import CInP

class API:
  def __init__( self ):
    self.client = CInP( 'http://localhost:8888', '/api/v1/' )
    token = self.client.call( '/api/v1/Auth/User(login)', { 'username': 'ui', 'password': 'ui' } )
    self.client.setAuth( 'ui', token )

  def getProducts( self ):
    return self.client.getFilteredObjects( '/api/v1/Products/Product' )

  def getCustomer( self ):
    uri = self.client.call( '/api/v1/Auth/User(customer)', {} )
    if uri is not None:
      return self.client.get( uri )
    else:
      return None

  def buy( self, product ): # product looks like "'/api/v1/Products/Product:1:'"
    return self.client.call( product + '(buy)' )

  def scan( self ):
    token = self.client.call( '/api/v1/Auth/User(login_via_camera)', {} )
    print( "Login token '{0}'".format( token ) )
    self.client.setAuth( '__Customer__', token )