catalog = {} 
def add_book(titulo, autor, isbn, genero):
  catalog[isbn] = {'titulo': titulo, 'autor': autor, 'genero': genero}

def search_book(query):
  results = []
  for isbn, book_data in catalog.items():
    if query in book_data['titulo'] or query in book_data['autor'] or query == isbn:
      results.append(book_data)
  return results

def display_catalog():
  for isbn, book_data in catalog.items():
    print(f"ISBN: {isbn}, Titulo: {book_data['titulo']}, Autor: {book_data['autor']}, Genero: {book_data['genero']}")

# Example usage
add_book("The Lord of the Rings", "J.R.R. Tolkien", "9780547928227", "Fantasy")
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803", "Science Fiction")
add_book("Harry Potter and the Order of the Phoenix", "J. K. Rowling", "9788498383621", "Fantasy")
search_results = search_book("Tolkien")
print(search_results)

display_catalog()