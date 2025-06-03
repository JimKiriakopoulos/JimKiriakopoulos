"""Μικρή αφήγηση στα ελληνικά για μια εφαρμογή που κάνει τα όνειρα πραγματικότητα."""

# Οι χαρακτήρες της ιστορίας
characters = {
    "Νίκος": "ο νεαρός προγραμματιστής",
    "Ελένη": "η φίλη του Νίκου και συνεργάτης",
    "Μαρία": "η γυναίκα στα μέσα της ζωής",
    "Ιωάννης": "ο συνταξιούχος καθηγητής ιστορίας",
}


def create_dream_app() -> str:
    """Δημιουργεί την εφαρμογή που φέρνει τα όνειρα στη ζωή."""
    print(
        f"{characters['Νίκος']} και {characters['Ελένη']} δημιουργούν μια εφαρμογή "
        "που επιτρέπει στους χρήστες να 'ζουν' τα όνειρά τους."
    )
    return "dream_app"


def live_dream(character_desc: str, app: str) -> None:
    """Η Μαρία βιώνει την εμπειρία της νεότητας."""
    print(
        f"{character_desc} χρησιμοποιεί την {app} για να 'ζήσει' το όνειρο "
        "της νεότητας."
    )


def share_stories(teacher_desc: str) -> None:
    """Ο κύριος Ιωάννης μοιράζεται τις αναμνήσεις του."""
    print(f"{teacher_desc} μοιράζεται τις ιστορίες του από το παρελθόν.")


def connect_generations(app: str) -> None:
    """Προσθέτει λειτουργία που ενώνει τις γενιές."""
    print(
        f"{characters['Νίκος']} και {characters['Ελένη']} προσθέτουν μια νέα "
        f"λειτουργία στην {app} για να ενώσουν τις γενιές."
    )


def main() -> None:
    """Τρέχει την αφήγηση της ιστορίας."""
    dream_app = create_dream_app()
    live_dream(characters["Μαρία"], dream_app)
    share_stories(characters["Ιωάννης"])
    connect_generations(dream_app)


if __name__ == "__main__":
    main()
