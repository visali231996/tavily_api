package dataservice

import (
	"APIS/model"
	"database/sql"
)

func DeleteBook(db *sql.DB, book model.Book) error {
	query := "DELETE FROM books WHERE id=?"
	_, err := db.Exec(query, book.Id)
	if err != nil {
		return err
	}
	return nil
}

func CreateBook(db *sql.DB, book model.Book) error {
	query := "INSERT INTO books(id,author,title,year) VALUES(?,?,?,?) "
	_, err := db.Exec(query, book.Id, book.Author, book.Title, book.Year)
	if err != nil {
		return err
	}
	return nil
}

func UpdateBook(db *sql.DB, book model.Book) error {
	query := "UPDATE books SET author=? WHERE id = ?; "
	_, err := db.Exec(query, book.Author, book.Id)
	if err != nil {
		return err
	}
	return nil
}

func ListBook(db *sql.DB, book model.Book) error {
	query := "SELECT * FROM books where id=? "
	_, err := db.Exec(query, book.Id)
	if err != nil {
		return err
	}
	return nil
}


