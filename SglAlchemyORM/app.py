import customtkinter as ctk
from alchemy_orm import Author
from orm_connection import Session
from CTkTable import CTkTable


def add_author():
    print("Dodaje autora")


if __name__ == '__main__':
    # ctk.set_appearance_mode('dark')
    app = ctk.CTk()
    app.title = 'Biblioteka'
    app.geometry('1024x700')

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)

    menu_bar = ctk.CTkFrame(app, corner_radius=20)
    menu_bar.grid_columnconfigure(0, weight=1)
    menu_bar.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

    app_title = ctk.CTkLabel(menu_bar, text='Biblioteka', font=ctk.CTkFont(size=15, weight='bold'))
    app_title.grid(row=0, column=0, padx=10, pady=10)

    add_author_button = ctk.CTkButtton(menu_bar, text='Dodaj Autora')
    add_author_button.grid(row=0, column=1, padx=25, pady=10)

    app_content = ctk.CTkFrame(app)
    app_content.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    authors = session.execute(select(Author)).scalars().all()
    author_data = [['ID', 'Imie', 'Drugie imie', 'Email', 'Login']] +\
        [[a.id, a.name, a.middle, a.email, a.login]for a in authors]
    author_table = CTkTable(author_data)
    authors_table = CTkTable(master==app_content, rows=len(authors), value = colums= len(authors_data(0))


    app.mainloop()

