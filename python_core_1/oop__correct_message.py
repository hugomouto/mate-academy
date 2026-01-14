class CorrectMessage:
    def __init__(self, message: str) -> None:
        self.message = message

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        self._message = message.capitalize()
 