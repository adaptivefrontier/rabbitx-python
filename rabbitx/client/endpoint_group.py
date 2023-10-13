from rabbitx-python.client.session import ClientSession


class EndpointGroup:

    session: ClientSession

    def __init__(self, session: ClientSession):
        self.session = session
