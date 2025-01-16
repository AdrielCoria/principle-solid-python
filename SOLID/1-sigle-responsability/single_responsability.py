'''
El usuario debe poder ser capaz de hacer varias acciones, por ejemplo guardar el usuario.
'''
# ----------------------------------------------------------------
#                      GESTIÓN DE USUARIOS
# ----------------------------------------------------------------
# FORMA INCORRECTA
class User:
    
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        
    def save_to_database(self):
        # Código para guardar el usuario en la base de datos.
        pass
    
    def send_email(self):
        # Se desea enviar un email.
        pass
    
    
# FORMA CORRECTA
class User:
    
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class UserService:
    
    def save_to_database(self, user):
        # Guardamos el usuario en la base de datos.
        pass
    
class EmailService:
    
    def send_email(self, email, message):
        # Enviamos el mail
        pass
    
# ----------------------------------------------------------------
#                      GESTIÓN DE PRESTAMOS DE LIBROS
# ----------------------------------------------------------------

# FORMA INCORRECTA

class Library:
    
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = [] # prestamo
        
    
    # Agregamos libros
    def add_book(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})
    
    def add_user(self, name, id, email):
        self.books.append({"name": name, "id": id, "email": email})    
        
    def loans_book(self, user_id, book_title): # Prestar un libro
        for book in self.books:
            if book["title"] == book_title and book["copias"] > 0:
                book["copias"] -= 1
                self.loans.append({"user_id": user_id, "book_title": book_title}) # Creamos estructuras -> Diccionarios
                return True
            return False # El libro no esta disponible

    def return_book(self, user_id, book_title): # Devolver un libro
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copias"] +=1
                    return True
        return False


# FORMA CORRECTA

class Book:
    
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class User:
    
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email
        
class Loan:
    
    def __init__(self):
        self.loans = []
        
    def loans_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append({"user_id": user.id, "book_title": book.title})
            return True
        return False
    
    def return_book(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False
        
class Library:
    
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()
        
    
    # Agregamos libros
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self,user):
        self.books.append(user)    
        
    def loans_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if user and book:
            return self.loans_service.loans_book(user, book)
        return False

    def return_book(self, user_id, book_title): # Devolver un libro
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if user and book:
            return self.loans_service.return_book(user, book)
        return False 
        
