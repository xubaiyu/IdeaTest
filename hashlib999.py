
import hashlib

a = "a test string"
print( 'md5 = %s' % (hashlib.md5(a.encode()).hexdigest(),) )
print( 'sha1 = %s' % (hashlib.sha1(a.encode()).hexdigest(),) )
print ('sha224 = %s' % (hashlib.sha224(a.encode()).hexdigest(),) )
print( 'sha256 = %s' % (hashlib.sha256(a.encode()).hexdigest(),) )
print ('sha384 = %s' % (hashlib.sha384(a.encode()).hexdigest(),) )
print( 'sha512 = %s' % (hashlib.sha512(a.encode()).hexdigest(),) )