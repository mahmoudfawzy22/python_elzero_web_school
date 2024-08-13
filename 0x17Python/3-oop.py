class Message:

    @classmethod
    def print_message(cls) :
        return f"Hello From Class {cls.__name__}"

print(Message.print_message())

# Output
# Hello From Class Message