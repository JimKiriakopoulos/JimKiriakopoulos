# Η ιστορία της πόλης των ονείρων

# Οι χαρακτήρες της ιστορίας
characters = {
    "Νίκος": " ο νεαρός προγραμματιστής",
    "Ελένη": " η φίλη του Νίκου και συνεργάτης",
    "Μαρία": " η γυναίκα στα μέσα της ζωής",
    "Ιωάννης": " ο συνταξιούχος καθηγητής ιστορίας"
}

# Η εφαρμογή που φέρνει τα όνειρα στη ζωή
def create_dream_app():
    # Ο Νίκος και η Ελένη δημιουργούν την εφαρμογή
    print(f"{characters['Νίκος']} και {characters['Ελένη']} δημιουργούν μια εφαρμογή που επιτρέπει στους χρήστες να 'ζουν' τα όνειρά τους.")
    return "dream_app"

# Η Μαρία "ζει" το όνειρό της
def live_dream(character, app):
    # Η Μαρία βιώνει την εμπειρία της νεότητας
    print(f"{character} χρησιμοποιεί την {app} για να 'ζήσει' το όνειρο της νεότητας.")

# Ο κύριος Ιωάννης μοιράζεται τις ιστορίες του
def share_stories(teacher):
    # Ο κύριος Ιωάννης μοιράζεται τις αναμνήσεις του
    print(f"{teacher} μοιράζεται τις ιστορίες του από το παρελθόν.")

# Η εφαρμογή ενώνει τις γενιές
def connect_generations(app):
    # Ο Νίκος και η Ελένη προσθέτουν μια νέα λειτουργία
    print(f"{characters['Νίκος']} και {characters['Ελένη']} προσθέτουν μια νέα λειτουργία στην {app} για να ενώσουν τις γενιές.")

# Η αφήγηση της ιστορίας
dream_app = create_dream_app()
live_dream(characters['Μαρία'], dream_app)
share_stories(characters['Ιωάννης'])
connect_generations(dream_app)

