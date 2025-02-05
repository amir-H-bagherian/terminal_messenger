from abc import ABC

from utilitis.get_input import get_input


class Node:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.children = []
        assert parent is None or isinstance(parent, Node)  # parent must be node
        self.parent = parent
        if parent:
            self.parent.children.append(self)


class Menu(ABC, Node):
    def __init__(self, name, parent=None, description=""):
        Node.__init__(self, name, parent)  # TODO: use super
        self.description = description

    def __call__(self, *args, **kwargs):
        pass

    def get_input(self, prompt, validator):
        return get_input(prompt, validator)

    def __repr__(self):
        return f"{self.name}\n{self.description}"


class MenuList(Menu):
    def __call__(self, *args, **kwargs):
        print(f'{self.parent.name} > {self.name}' if self.parent else self.name)
        print(f'{self.description}')
        print("\nMenu items:")
        for id_menu, sub_menu in enumerate(self.children):
            print(f"\t{id_menu + 1}.{repr(sub_menu)}")

        def validator(s: str):
            if s.isnumeric():
                s = int(s)
                return self.children[s - 1] if s else self.parent
            else:
                for child in self.children:
                    if child.name.strip().casefold == s.strip().casefold():
                        return child

        prompt = f"\nSelect next menu (0 to {'return' if self.parent else 'exit'}):"
        # next_menu = self.get_input(prompt)
        next_menu = self.get_input(prompt, validator=validator)
        if not next_menu:
            exit(0)
        else:
            next_menu()


class MenuView(Menu):
    def __init__(self,  name,function, parent=None, description=""):
        super().__init__(name, parent, description)
        self.function = function

    def __call__(self, *args, **kwargs):
        print(f'{self.parent.name} > {self.name}' if self.parent else self.name)
        print(f'{self.description}')
        print("\nMenu items:")
        # To separate and choose children who fit some criteria.
        eligible_children = list(filter(lambda child: child.condition(), self.children))
        for id_menu, sub_menu in enumerate(eligible_children):
            print(f"\t{id_menu + 1}.{repr(sub_menu)}")

        def validator(s: str):
            if s.isnumeric():
                s = int(s)
                return self.children[s - 1] if s else self.parent
            else:
                for child in self.children:
                    if child.name.strip().casefold == s.strip().casefold():
                        return child

        self.function(*args, **kwargs)

        prompt = f"\nSelect next menu (0 to {'return' if self.parent else 'exit'}):"
        # next_menu = self.get_input(prompt)
        next_menu = self.get_input(prompt, validator=validator)
        if not next_menu:
            exit(0)
        else:
            next_menu()

    def __repr__(self):
        return f"{self.name}\n{self.description}"
