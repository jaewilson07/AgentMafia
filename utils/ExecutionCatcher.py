def generate_error_message(message=None, exception=None):

    if exception:
        if message == None:
            message = str(exception)

        template = f"An exception of type {type(exception) and type(exception).__name__ or 'unknown'} occurred."

        if exception.args:
            template += f" Arguments: {','.join(str(arg) for arg in exception.args if arg and str(arg))}"

        message = f"{message}\n{template}"

    if not message.startswith("💀"):
        message = "💀  " + message


class RagException(Exception):
    def __init__(self, message=None, exception=None):

        super().__init__(generate_error_message(message=message, exception=exception))
