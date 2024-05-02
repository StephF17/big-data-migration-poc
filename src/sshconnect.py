import os
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv

load_dotenv()

def create_tunnel():
    try:
        server = SSHTunnelForwarder(
            (os.getenv('SSH_HOST'), int(os.getenv('SSH_PORT'))),
            ssh_username=os.getenv('SSH_USER'),
            ssh_pkey=os.getenv('SSH_KEYFILE'),
            remote_bind_address=(os.getenv('DB_HOST'), int(os.getenv('DB_PORT'))),
            local_bind_address=(os.getenv('LOCALHOST'), int(os.getenv('DB_PORT')))
        )
        #server.skip_tunnel_checkup = False
        server.start()
        print("SSH tunnel established successfully:")
        print(server.tunnel_is_up)
        return server
    except Exception as ex:
        print("Error establishing SSH tunnel.")
        raise ex
    
def close_tunnel(server):
    if server:
        server.stop()
        print("SSH tunnel closed.")