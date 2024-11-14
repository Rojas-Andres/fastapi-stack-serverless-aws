class BaseException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(Exception): ...


class UserAlreadyExistsException(BaseException): ...


class UserPasswordInvalid(Exception): ...


class ValidationError(BaseException): ...
