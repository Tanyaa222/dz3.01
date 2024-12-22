from colorama import init, Fore
init()
class DemoClass:
    """
    Клас для демонстрації роботи з атрибутами та методами.
    """
    def __init__(self, message):
        self.message = message
    def print_message(self):
        """Виведення повідомлення зеленим кольором."""
        print(Fore.GREEN + self.message + Fore.RESET)
    def print_uppercase_message(self):
        """Виведення повідомлення у верхньому регістрі жовтим кольором."""
        print(Fore.YELLOW + self.message.upper() + Fore.RESET)
def inspect_class(cls):
    """Перегляд атрибутів та методів класу."""
    print(Fore.CYAN + f"Клас: {cls.__name__}" + Fore.RESET)
    for item in dir(cls):
        if not item.startswith("_"):  # Ігноруємо службові методи
            print(Fore.YELLOW + f" - {item}" + Fore.RESET)
if __name__ == "__main__":
    demo = DemoClass("Привіт, світ!")
    demo.print_message()
    demo.print_uppercase_message()
    inspect_class(DemoClass)
