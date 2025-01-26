class Config:
    AdminPublicKey: bytes = bytes(32)
    ServerUrl: str = "http://localhost:14513/"
    maxInputData: int = 2**24-1
