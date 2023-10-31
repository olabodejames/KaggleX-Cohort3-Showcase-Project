// Get the table element
var table = document.getElementById("myTable");

// Get the number of rows per page
var rowsPerPage = 10;

// Get the current page number
var currentPage = 1;

// Get the total number of pages
function getTotalPages() {
  // Get the total number of rows in the table body
  var totalRows = table.tBodies[0].rows.length;

  // Return the ceiling of the division of total rows by rows per page
  return Math.ceil(totalRows / rowsPerPage);
}

// Display the current page of data
function displayPage() {
  // Get the start index and end index of the current page
  var startIndex = (currentPage - 1) * rowsPerPage;
  var endIndex = currentPage * rowsPerPage;

  // Loop through all the rows in the table body
  for (var i = 0; i < table.tBodies[0].rows.length; i++) {
    // If the row index is within the current page range, show the row
    if (i >= startIndex && i < endIndex) {
      table.tBodies[0].rows[i].style.display = "";
    }
    // Otherwise, hide the row
    else {
      table.tBodies[0].rows[i].style.display = "none";
    }
  }
}

// Update the pagination buttons
function updateButtons() {
  // Get the previous and next buttons
  var prevButton = document.getElementById("prev");
  var nextButton = document.getElementById("next");

   // If the current page is the first page, disable the previous button
   if (currentPage == 1) {
     prevButton.disabled = true;
   }
   // Otherwise, enable it
   else {
     prevButton.disabled = false;
   }

   // If the current page is the last page, disable the next button
   if (currentPage == getTotalPages()) {
     nextButton.disabled = true;
   }
   // Otherwise, enable it
   else {
     nextButton.disabled = false;
   }
}

// Add a click event listener to the previous button
document.getElementById("prev").addEventListener("click", function() {
   // Decrease the current page by one
   currentPage--;

   // Display the new page of data
   displayPage();

   // Update the pagination buttons
   updateButtons();
});

// Add a click event listener to the next button
document.getElementById("next").addEventListener("click", function() {
   // Increase the current page by one
   currentPage++;

   // Display the new page of data
   displayPage();

   // Update the pagination buttons
   updateButtons();
});

// Display the first page of data
displayPage();

// Update the pagination buttons
updateButtons();
