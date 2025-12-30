const notice = (msg) => new Notice(msg, 5000);
const log = (msg) => console.log(msg);

const GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes";

module.exports = async function start(params) {
  const { quickAddApi: qa, app } = params;

  // Get search query from clipboard or user input
  let clipBoardContents = await qa.utility.getClipboard();
  const query = await qa.inputPrompt(
    "Enter Book title, author, or ISBN:",
    clipBoardContents,
    clipBoardContents
  );
  
  if (!query) {
    notice("No search query entered.");
    throw new Error("No search query entered.");
  }

  notice("Searching Google Books...");
  
  // Search Google Books
  const encodedQuery = encodeURIComponent(query);
  const searchURL = `${GOOGLE_BOOKS_API_URL}?q=${encodedQuery}&maxResults=20`;
  
  let response;
  try {
    response = await fetch(searchURL);
  } catch (error) {
    notice("Failed to connect to Google Books API");
    throw new Error("Network error: " + error.message);
  }
  
  const data = await response.json();
  
  if (!data.items || data.items.length === 0) {
    notice("No books found for that query.");
    throw new Error("No books found.");
  }

  // Create choices for suggester with title, author, and year
  const bookChoices = data.items.map(item => {
    const info = item.volumeInfo;
    const title = info.title || "Unknown Title";
    const authors = info.authors ? info.authors.join(", ") : "Unknown Author";
    const year = info.publishedDate ? info.publishedDate.substring(0, 4) : "N/A";
    return `${title} - ${authors} (${year})`;
  });

  // Let user select the correct book
  const selectedIndex = bookChoices.indexOf(
    await qa.suggester(bookChoices, bookChoices, "Select the correct book:")
  );
  
  if (selectedIndex === -1) {
    notice("No book selected.");
    throw new Error("No book selected.");
  }

  const selectedBook = data.items[selectedIndex];
  const info = selectedBook.volumeInfo;
  
  // Extract all useful information
  const bookData = {
    // Basic info
    title: info.title || "",
    subtitle: info.subtitle || "",
    authors: info.authors || [],
    authorsString: info.authors ? info.authors.join(", ") : "",
    
    // Publication details
    publisher: info.publisher || "",
    publishedDate: info.publishedDate || "",
    publishedYear: info.publishedDate ? info.publishedDate.substring(0, 4) : "",
    
    // Description
    description: info.description || "",
    
    // Identifiers
    isbn10: "",
    isbn13: "",
    googleBooksId: selectedBook.id || "",
    
    // Categories and subjects
    categories: info.categories || [],
    categoriesString: info.categories ? info.categories.join(", ") : "",
    
    // Physical details
    pageCount: info.pageCount || "",
    language: info.language || "",
    
    // Images
    thumbnailSmall: info.imageLinks?.smallThumbnail || "",
    thumbnail: info.imageLinks?.thumbnail || "",
    thumbnailLarge: info.imageLinks?.large || info.imageLinks?.medium || info.imageLinks?.thumbnail || "",
    
    // Links
    previewLink: info.previewLink || "",
    infoLink: info.infoLink || "",
    canonicalVolumeLink: info.canonicalVolumeLink || "",
    
    // Additional metadata
    maturityRating: info.maturityRating || "",
    averageRating: info.averageRating || "",
    ratingsCount: info.ratingsCount || "",
    
    // File name safe version
    fileName: replaceIllegalFileNameCharactersInString(info.title || "Untitled"),
  };
  
  // Extract ISBNs
  if (info.industryIdentifiers) {
    info.industryIdentifiers.forEach(id => {
      if (id.type === "ISBN_10") {
        bookData.isbn10 = id.identifier;
      } else if (id.type === "ISBN_13") {
        bookData.isbn13 = id.identifier;
      }
    });
  }
  
  // Set variables for QuickAdd template
  params.variables = bookData;
  
  notice(`Book "${bookData.title}" loaded successfully!`);
  
  return bookData;
}

function replaceIllegalFileNameCharactersInString(string) {
  return string.replace(/[\\,#%&\{\}\/*<>?$\'\":@]/g, "");
}