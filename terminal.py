import questionary
from questionary import Style


def select_from_list(options, title="Select an option"):
    custom_style = Style(
        [
            ("qmark", "fg:#673ab7 bold"),
            ("question", "bold"),
            ("pointer", "fg:#ffd700 bold"),
            ("highlighted", "fg:#ffd700 bold"),
            ("selected", "fg:#cc5454"),
            ("instruction", "fg:#888888 italic"),
        ]
    )

    choice = questionary.select(
        title + ":",
        choices=options,
        style=custom_style,
        instruction="(Use arrow keys to navigate, Enter to select)",
    ).ask()

    return choice