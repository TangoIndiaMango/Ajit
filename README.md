# Ajit
Api requirements
- Retrieve books meeting zero or more filter criteria
- Return the number of books meeting the criteria and a list of book objects containing title, author information, genre, language, subject(s), bookshelf(s), and links to download the book in available formats (mime-types)
- If the number of books exceeds 25, return 25 at a time and support retrieving the next sets of 25 books until all are retrieved
- Return books in decreasing order of popularity (number of downloads)
- Return data in JSON format
- Support filtering on book ID numbers, language, mime-type, topic (on subject and bookshelf), author, and title
- Support multiple filter criteria and multiple filter values for each criteria
