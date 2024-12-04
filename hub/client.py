# generate cast message
# given is text, signer
from datetime import datetime
from message_pb2 import CastAddBody, MessageData, Message, MessageType, FarcasterNetwork, HashScheme, SignatureScheme
from blake3 import blake3
from nacl.signing import SigningKey
import requests
from core.config import logger

HUB_URL = "https://hub.farcaster.standardcrypto.vc:2281/v1/submitMessage"
# HUB_URL = "https://hub.pinata.cloud/v1/validateMessage"
FARCASTER_EPOCH = 1609459200

def cast_message(text: str, signer: bytes, fid: int):

    # Prepare signing key
    signing_key = SigningKey(signer)

    # prepare cast add body
    cast_add_body = CastAddBody()
    cast_add_body.text = text
    # cast_add_body.type = CastType.CAST
    # prepare message data
    msg_data = MessageData()
    msg_data.type = MessageType.MESSAGE_TYPE_CAST_ADD
    msg_data.fid = fid
    msg_data.timestamp = int(datetime.now().timestamp()) - FARCASTER_EPOCH
    msg_data.network = FarcasterNetwork.FARCASTER_NETWORK_MAINNET
    msg_data.cast_add_body.CopyFrom(cast_add_body)

    msg_data_bytes = msg_data.SerializeToString()
    # Prepare message
    msg = Message()
    msg.signer = signing_key.verify_key.encode()
    msg.hash = blake3(msg_data_bytes).digest()[:20] # 20 bytes hash
    msg.hash_scheme = HashScheme.HASH_SCHEME_BLAKE3
    msg.signature = signing_key.sign(msg.hash).signature
    # msg.signature = signing_key.sign(msg_data_bytes).signature
    msg.signature_scheme = SignatureScheme.SIGNATURE_SCHEME_ED25519
    msg.data.CopyFrom(msg_data)
    msg.data_bytes = msg_data_bytes
    return msg.SerializeToString()

def submit_message(message: bytes):
    response = requests.post(HUB_URL, headers={"Content-Type": "application/octet-stream"}, data=message)
    logger.info(response.status_code)
    logger.info(response.json())
    
# if __name__ == "__main__":

#     msg_bytes = cast_message(
#         "Back, again", 
#         bytes.fromhex("86eeb46463702350cabe18945705583e8e5f25ffd2e9b05abeb52de443064c4e"),
#         880577
#     )
#     submit_message(msg_bytes)
