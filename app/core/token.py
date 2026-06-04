from datetime import timedelta, datetime
from jose import jwt , JWTError
import uuid
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRY_MIN = settings.ACCESS_TOKEN_EXPIRY_MIN

def create_access_token(  #user for short time like minutes
        user_id: int,
        role:str,
        expiry:timedelta = None,
        refresh : bool = False):

    payload = {
        "user_id": user_id, #means subject of token so token belongs to this xyz userid user
        "role":role,
        "exp" : datetime.utcnow() + (
            expiry if expiry is not None else timedelta(minutes = ACCESS_TOKEN_EXPIRY_MIN)
        ), #means after 30 min token expires
        "jti" : str(uuid.uuid4()), #a unique id for this exact token not user like serial number
        "refresh" : refresh # cannot be user for days thats why refrsh = false | # long lives days or weeks
    }

    token = jwt.encode( #converts payload signs using secrete key
        payload,
        SECRET_KEY,
        algorithm= ALGORITHM
    )
    return token


def decode_token(token : str) ->dict:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )
        return payload
    except JWTError as exc:
        logger.warning("JWT decode failed", exc_info=exc)
        return None



