from streamlit_authenticator.utilities.hasher import Hasher

hashed_pw = Hasher.hash(["123456"])
print(hashed_pw)
