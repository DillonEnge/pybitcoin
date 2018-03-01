from .privatekey import BitcoinPrivateKey

class GarlicoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 38

class LitecoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 48

class AddressFetcher():
    class GarlicoinPrivateKey(BitcoinPrivateKey):
        _pubkeyhash_version_byte = 38

    class LitecoinPrivateKey(BitcoinPrivateKey):
        _pubkeyhash_version_byte = 48

    def __init__(self, app=None):
        self.app = app

    def generateGarlicAddress(self, private = False):
        private_key = BitcoinPrivateKey()
        public_key = private_key.public_key()
        garlicoin_private_key = GarlicoinPrivateKey(private_key.to_hex())
        garlicoin_public_key = garlicoin_private_key.public_key()
        if private:  
            return [garlicoin_public_key.address(), garlicoin_private_key.to_hex()]
        return garlicoin_public_key.address()

    def generateLiteAddress(self, private = False):
        private_key = BitcoinPrivateKey()
        public_key = private_key.public_key()
        litecoin_private_key = LitecoinPrivateKey(private_key.to_hex())
        litecoin_public_key = litecoin_private_key.public_key()
        if private: 
            return [litecoin_public_key.address(), litecoin_private_key.to_hex()]
        return litecoin_public_key.address()