const cardData = [
    {
        title: "Shirt 1",
        content: "Black T-Shirt",
        price: "₹100 -/",
        imageUrl: "static/images/1.png",
        Description: "This stylish t-shirt features the phrase 'Mind is a weapon and it's not a weapon' printed boldly across the chest in a modern font. Made from high-quality cotton material, this t-shirt is comfortable to wear and easy to care for, making it a versatile addition to any wardrobe. Whether you're hitting the gym, running errands, or simply relaxing at home, this t-shirt is sure to make a statement and inspire those around you."
    },
    {
        title: "Shirt 2",
        content: "Black T-Shirt",
        price: "₹300 -/",
        imageUrl: "static/images/2.jpg",
        Description: " This stylish t-shirt features the phrase Mind is a weapon and it's not a weapon printed boldly across the chest in a modern font,  Made from high-quality cotton material, this t-shirt is comfortable to wear and easy to care for, making it a versatile addition to any wardrobe Whether you re hitting the gym, running errands, or simply relaxing at home, this t-shirt is sure to make a statement and inspire those around you"
    },
    {
        title: "Shirt 3",
        content: "Black T-Shirt",
        price: "₹500 -/",
        imageUrl: "static/images/3.jpg",
        Description: " This stylish t-shirt features the phrase Mind is a weapon and it's not a weapon printed boldly across the chest in a modern font,  Made from high-quality cotton material, this t-shirt is comfortable to wear and easy to care for, making it a versatile addition to any wardrobe Whether you re hitting the gym, running errands, or simply relaxing at home, this t-shirt is sure to make a statement and inspire those around you"
    },
    {
        title: "Shirt 4",
        content: "Black T-Shirt",
        price: "₹400 -/",
        imageUrl: "static/images/4.jpg",
        Description: " This stylish t-shirt features the phrase Mind is a weapon and it's not a weapon printed boldly across the chest in a modern font,  Made from high-quality cotton material, this t-shirt is comfortable to wear and easy to care for, making it a versatile addition to any wardrobe Whether you re hitting the gym, running errands, or simply relaxing at home, this t-shirt is sure to make a statement and inspire those around you"
    },
    {
        title: "Shirt 5",
        content: "Black T-Shirt",
        price: "₹350 -/",
        imageUrl: "static/images/5.jpg"
    },
    {
        title: "Shirt 6",
        content: "Black T-Shirt",
        price: "₹450 -/",
        imageUrl: "static/images/6.jpg"
    },
    {
        title: "Shirt 7",
        content: "Black T-Shirt",
        price: "₹650 -/",
        imageUrl: "static/images/7.jpg"
    },
    {
        title: "Shirt 8",
        content: "Black T-Shirt",
        price: "₹250 -/",
        imageUrl: "static/images/8.jpg"
    },
    {
        title: "Shirt 9",
        content: "Black T-Shirt",
        price: "₹150 -/",
        imageUrl: "static/images/DE_01.png"
    },
    {
        title: "Shirt 10",
        content: "Black T-Shirt",
        price: "₹450 -/",
        imageUrl: "static/images/DE_02.png"
    }
];

const shirtData = {
    shirtBase: "path/to/your/base_shirt.png",
    customizableElements: [],
};

const cardsPerPage = 4;
let currentPage = 1;

const cartDataKey = 'cartData';
let cart = [];


let isFirstItemAdded = true;

function createCards(data) {
    const container = document.getElementById('cardContainer');
    container.innerHTML = '';
    data.forEach((card, index) => {
        const cardHTML = generateCard(card, index); 
        container.innerHTML += cardHTML;
        console.log("Index inside generateCard:", index); 
    });
    displayCards(currentPage);
}

function setupPagination() {
    const numPages = Math.ceil(cardData.length / cardsPerPage);
    const paginatedContainer = document.getElementById('pagination');
    paginatedContainer.innerHTML = '';

    const prevButton = document.createElement('li');
    prevButton.classList.add('page-item');
    const prevLink = document.createElement('a');
    prevLink.classList.add('page-link');
    prevLink.href = '#';
    prevLink.textContent = 'Previous';
    prevButton.appendChild(prevLink);
    prevButton.addEventListener('click', function () {
        if (currentPage > 1) {
            currentPage--;
            displayCards(currentPage);
            highlightCurrentPage();
        }
    });
    paginatedContainer.appendChild(prevButton);

    for (let i = 1; i <= numPages; i++) {
        const pageButton = document.createElement('li');
        pageButton.classList.add('page-item');
        const pageLink = document.createElement('a');
        pageLink.classList.add('page-link');
        pageLink.href = '#';
        pageLink.textContent = i;
        pageLink.addEventListener('click', function () {
            currentPage = i;
            displayCards(currentPage);
            highlightCurrentPage();
        });
        pageButton.appendChild(pageLink);
        paginatedContainer.appendChild(pageButton);
    }

    const nextButton = document.createElement('li');
    nextButton.classList.add('page-item');
    const nextLink = document.createElement('a');
    nextLink.classList.add('page-link');
    nextLink.href = '#';
    nextLink.textContent = 'Next';
    nextButton.appendChild(nextLink);
    nextButton.addEventListener('click', function () {
        if (currentPage < numPages) {
            currentPage++;
            displayCards(currentPage);
            highlightCurrentPage();
        }
    });
    paginatedContainer.appendChild(nextButton);
    highlightCurrentPage();
}

function highlightCurrentPage() {
    const paginationLinks = document.querySelectorAll('#pagination a');
    paginationLinks.forEach(link => {
        link.classList.remove('active');
        if (parseInt(link.textContent) === currentPage) {
            link.classList.add('active');
        }
    });
}

console.log(cardData);
document.querySelectorAll('.openModalBtn').forEach((button, index) => {
    button.addEventListener('click', () => {
        console.log("Clicked button index:", index);
        console.log("Card data:", cardData[index]);
        openModal(cardData[index]);
    });
});

function openModal(cardData) {
    console.log("Card Data:", cardData);
    console.log("Image URL:", cardData.imageUrl); 
    console.log("Description:", cardData.Description); 

    const modal = document.getElementById('modal');
    const modalContent = modal.querySelector('.modal-content');
    const modalTitle = modalContent.querySelector('#modalTitle');
    const modalImage = modalContent.querySelector('#modalImage');
    const modalDescription = modalContent.querySelector('#modalDescription');
    const modalPrice = modalContent.querySelector('#modalPrice');

    modalTitle.textContent = cardData.title || '';
    modalImage.src = cardData.imageUrl || '';
    modalDescription.textContent = cardData.Description || ''; 
    modalPrice.textContent = cardData.price || '';

    modalContent.style.width = "60%";
    modalContent.style.height = "400px";
    
    modalImage.style.height = "200px";

    modalDescription.style.display = "inline-block";
    modalDescription.style.verticalAlign = "top";
    

    modal.style.display = "block";
}
function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

function displayCards(page) {
    const startIndex = (page - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;
    console.log("Start Index:", startIndex, "End Index:", endIndex);

    const container = document.getElementById('cardContainer');
    container.innerHTML = '';

    const paginatedCards = cardData.slice(startIndex, endIndex);
    console.log("Paginated Cards:", paginatedCards);

    paginatedCards.forEach(card => {
        const cardHTML = generateCard(card);
        container.innerHTML += cardHTML;
    }); 
    document.querySelectorAll('.openModalBtn').forEach((button, index) => {
        button.addEventListener('click', () => {
            openModal(cardData[index]);
        });
    })
}

function generateCard(card, index) {
    console.log("Index:", index); 
    return `
        <div class="card">
            <img src="${card.imageUrl}" alt="${card.title}">
            <div class="card-content">
                <h2 class="card-title">${card.title}</h2>
                <p class="card-text">${card.content}</p>
                <p class="card-price">${card.price}</p>
                <button class="openModalBtn view-details-btn" data-index="${index}">View Details</button>
                <button class="add-to-cart-btn" onclick="addToCart('${card.title}', '${card.price}', '${card.imageUrl}')">Add to Cart</button>
            </div>
        </div>
    `;
}

cart = JSON.parse(localStorage.getItem('cart')) || [];
function saveCartToStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
}


document.addEventListener('DOMContentLoaded', function() {
    initializeCart(); // Initialize the cart
    createCards(cardData); // Create the product cards
    setupPagination(); // Setup pagination

    // Attach event listeners to the "Add to Cart" buttons
    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', addToCartButtonClick);
    });

    displayCart(); // Display the cart
});

// Function to handle "Add to Cart" button clicks
function addToCartButtonClick(event) {
    console.log("Add to cart button clicked.");
    const cardIndex = event.target.dataset.index;
    addToCart(cardData[cardIndex].title, cardData[cardIndex].price, cardData[cardIndex].imageUrl);
}



function addToCart(title, price, imageUrl) {
    const numericPrice = parseFloat(price.replace('₹', '').trim());
    var existingItem = cart.find(item => item.title === title);
    if (existingItem) {
        existingItem.quantity += 1;
        existingItem.total = (existingItem.quantity * numericPrice).toFixed(2);
    } else {
        cart.push({ title: title, price: price, imageUrl: imageUrl, quantity: 1, total: numericPrice.toFixed(2) });
    }
    displayCart();
    displayCartTotal();
    updateCartTotal();
    saveCartToStorage();
    updateCartUI();
    updateCartIconAndCounter();
    const queryString = `?title=${encodeURIComponent(title)}&price=${encodeURIComponent(price)}&imageUrl=${encodeURIComponent(imageUrl)}`;
    updateCartCounter();
    displayNotification('Item added to cart: ' + title);
   updateCartTotalFromCartData();
    if (isFirstItemAdded) {
        displayNotification('Item added to cart: ' + title);
        isFirstItemAdded = false;
    }
    let count = parseInt(document.querySelector('#cart-total').textContent) || 0;
    count++;
    updateCartBadge(count);
    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', () => {
            const cardIndex = button.dataset.index;
            addToCart(cardData[cardIndex].title, cardData[cardIndex].price, cardData[cardIndex].imageUrl);
        });
    });
}


document.addEventListener('DOMContentLoaded', function() {
    displayCart();
});

function removeFromCart(title) {
    console.log("Removing item from cart:", title);
    const index = cart.findIndex(item => item.title === title);

    if (index !== -1) {
        const currentItem = cart[index];

        if (currentItem.quantity > 1) {
            currentItem.quantity--; // Decrease quantity by 1
            currentItem.total = (currentItem.quantity * parseFloat(currentItem.price.replace('₹', '').trim())).toFixed(2);
        } else {
            cart.splice(index, 1); // Remove item from cart if quantity is 1
        }

        displayCart();
        updateCartTotal();
        saveCartToStorage(); // Save updated cart to local storage
        updateCartUI();
        updateCartIconAndCounter();
    } else {
        console.log(`Item '${title}' not found in cart.`);
    }
    let count = parseInt(document.querySelector('#cart-total').textContent) || 0;
    if (count > 0) {
        count--;
        updateCartBadge(count); // Update cart badge count
    }
}


function saveCartCountToStorage(count) {
    localStorage.setItem('cartCount', count);
}

function displayCartTotal() {
    const totalElement = document.getElementById('cartTotal');
    if (totalElement) {
        const totalCost = calculateTotal();
        totalElement.textContent = '₹' + totalCost;
    } else {
        console.error("Cart total element not found.");
    }
}

function calculateTotalCost() {
    let totalCost = 0;
    cart.forEach(item => {
        const itemTotal = parseFloat(item.total.replace('₹', '').trim());
        if (!isNaN(itemTotal)) {
            totalCost += itemTotal;
        } else {
            console.error('Invalid total for item:', item);
        }
    });
    return totalCost.toFixed(2);
}

function updateTotalCost() {
    const totalCost = calculateTotalCost();
    const cartTotalElement = document.getElementById('cartTotal');
    if (cartTotalElement) {
        if (!isNaN(parseFloat(totalCost))) { 
            cartTotalElement.textContent = '₹' + parseFloat(totalCost).toFixed(2);
        } else {
            console.error('Invalid total cost:', totalCost);
        }
    } else {
        console.error('Cart total element not found.');
    }
}

function calculateTotal() {
    let total = 0;
    cart.forEach(item => {
        total += parseFloat(item.total);
    });
    return total.toFixed(2);
}

function updateCartTotal() {
    const totalCost = calculateTotal();
    console.log("Total Cost:", totalCost);
    const cartTotalElement = document.getElementById('cartTotal');
    if (cartTotalElement) {
        if (!isNaN(parseFloat(totalCost))) {
            cartTotalElement.textContent = '₹' + parseFloat(totalCost).toFixed(2);
            console.log("Total Cost:", totalCost);
        } else {
            console.error('Invalid total cost:', totalCost);
        }
    } else {
        console.error('Cart total element not found.');
    }
}

function clearCart() {
    cart = [];
    displayCart();
    displayCartTotal();
    updateCartTotal();
    saveCartToStorage();
}
    
window.onload = function() {
    updateCartTotal();
};
initializeCart();
displayCartTotal();

function loadCartFromStorage() {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
        displayCart();
        updateCartTotal();
        updateCartIconAndCounter();
    } else {
        cart = []; // If no cart data is found, initialize an empty cart
        displayCart(); // Display the empty cart
        updateCartTotal(); // Update the cart total
        updateCartIconAndCounter(); // Update the cart icon and counter
    }
}
function initializeCart() {
    if (localStorage.getItem('cart')) {
        cart = JSON.parse(localStorage.getItem('cart'));
        displayCart();
    }
    
    loadCartFromStorage();
    displayCart();
    updateCartIconAndCounter();
    updateCartBadge(0);
}



window.onload = initializeCart;

const parentElement = document.getElementById('parentElementId');

const cartTotalDiv = document.createElement('div');
cartTotalDiv.id = 'cartTotal';
cartTotalDiv.textContent = '₹0.00';


function displayCart() {
    console.log("Displaying cart...");
    const cartContainer = document.getElementById('cartContainer');
    if (cartContainer) {
        console.log("Cart container found.");
        // Create and append table element
        const table = document.createElement('table');
        table.classList.add('cart-table');

        // Create table header
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = `
            <th>Item</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
            <th>Action</th>
        `;
        table.appendChild(headerRow);

        // Iterate over cart items and create table rows for each item
        cart.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>
                    <div class="cart-item">
                        <img class="item-image" src="${item.imageUrl}" alt="${item.title}">
                        <div class="item-details">
                            <span class="item-title">${item.title}</span>
                        </div>
                    </div>
                </td>
                <td>${item.price}</td>
                <td>${item.quantity}</td>
                <td>${item.total}</td>
                <td><button class="remove-from-cart-btn" onclick="removeFromCart('${item.title}')">Remove</button></td>
            `;
            table.appendChild(row);
        });

        // Add total cost row
        const totalRow = document.createElement('tr');
        totalRow.innerHTML = `
            <td colspan="4">Total Cost:</td>
            <td id="cartTotal">₹${calculateTotalCost()}</td>
        `;
        table.appendChild(totalRow);

        // Add checkout button
        const checkoutButton = document.createElement('button');
        checkoutButton.id = 'checkoutButton';
        checkoutButton.className = 'btn checkout-btn';
        checkoutButton.textContent = 'Checkout';
        checkoutButton.addEventListener('click', checkout);
        const checkoutCell = document.createElement('td');
        checkoutCell.colSpan = 5;
        checkoutCell.appendChild(checkoutButton);
        const checkoutRow = document.createElement('tr');
        checkoutRow.appendChild(checkoutCell);
        table.appendChild(checkoutRow);

        // Append table to cart container
        cartContainer.innerHTML = ''; // Clear previous content
        cartContainer.appendChild(table);
    } else {
        console.error("Cart container element not found.");
    }
}
document.addEventListener('DOMContentLoaded', function() {
    const cartContainer = document.getElementById('cartContainer');

    if (cartContainer) {
        const emptyCartMessage = document.createElement('div');
        emptyCartMessage.textContent = 'Your cart is empty.';
        emptyCartMessage.style.fontWeight = 'bold';

        cartContainer.appendChild(emptyCartMessage);

        // Create the checkout button
        const checkoutButton = document.createElement('button');
        checkoutButton.textContent = 'Checkout';
        checkoutButton.addEventListener('click', function() {
            // Navigate to the checkout page
            window.location.href = 'payment-getway.html'; // Replace 'checkout.html' with the URL of your checkout page
        });

        // Append the checkout button to the cart container
        cartContainer.appendChild(checkoutButton);
    } else {
        console.error('Cart container element not found.');
    }
});



function generateCartItemRow(item) {
    const cartRow = document.createElement('tr');
    cartRow.classList.add('cart-row');

    const productCell = document.createElement('td');
    productCell.innerHTML = `<img src="${item.imageUrl}" alt="${item.title}" style="max-width: 100px; max-height: 100px;"> <span>${item.title}</span>`;
    cartRow.appendChild(productCell);

    const priceCell = document.createElement('td');
    priceCell.textContent = item.price;
    cartRow.appendChild(priceCell);

    const quantityCell = document.createElement('td');
    quantityCell.textContent = item.quantity;
    cartRow.appendChild(quantityCell);

    const actionCell = document.createElement('td');
    const removeButton = document.createElement('button');
    removeButton.classList.add('remove-from-cart-btn');
    removeButton.textContent = 'Remove';
    actionCell.appendChild(removeButton);
    cartRow.appendChild(actionCell);

    return cartRow;
}

// Assuming cart is defined elsewhere in your code

// Call displayCart function to display cart items
displayCart();


function checkout() {
    console.log("Checkout function called.");
    const totalAmount = localStorage.getItem('totalAmount');
    console.log("Total amount:", totalAmount);
    
    if (totalAmount > 0 && confirm("Are you sure you want to proceed with the payment?")) {
        cart = [];
        updateCartTotalFromCartData(); // Clear cart and update total amount in local storage
        
        displayCart(); // Update the cart display
        updateCartTotal(); // Update the cart total
        saveCartToStorage(); // Save the empty cart to local storage
        updateCartIconAndCounter(); // Update the cart icon and counter

        // Redirect to the payment gateway with the total amount
        window.location.href = `/paymentGetway?totalAmount=${totalAmount}`;
    } else {
        // Display a message or take appropriate action if the total amount is 0
        alert("Your cart is empty or the total amount is 0. Please add items to proceed with the payment.");
    }
}

function handleCheckout() {
    const totalCost = calculateTotalCost();
    console.log('Total Cost:', totalCost);

    const paymentForm = document.getElementById('paymentForm');
    if (paymentForm) {
        console.log('Payment Form Found:', paymentForm);
        const amountPaidField = paymentForm.querySelector('#AmountPaid');
        if (amountPaidField) {
            console.log('Amount Paid Field Found:', amountPaidField);
            amountPaidField.value = totalCost;
            paymentForm.submit();
        } else {
            console.error('Amount Paid Field Not Found.');
        }
    } else {
        console.error('Payment Form Not Found.');
    }
}
function updateCartTotalFromCartData() {
    let totalCost = 0;
    cart.forEach(item => {
        totalCost += parseFloat(item.total);
    });
    localStorage.setItem('totalAmount', totalCost.toFixed(2));
}

function updateCartIconAndCounter() {
    const cartCounter = document.getElementById('cartCounter');
    if (cartCounter) {
        if (cart.length > 0) {
            cartCounter.textContent = cart.length; // Show the count if cart is not empty
        } else {
            cartCounter.textContent = '0'; // Show '0' if cart is empty
        }
    } else {
        console.error('Cart counter element not found.');
    }
}

function updateCartBadge(count) {
    const badge = document.querySelector('#cart-total');
    badge.textContent = count;
    badge.style.display = count > 0 ? 'block' : 'none';
    saveCartCountToStorage(count); // Save cart count to local storage
}

function getCartCount() {
    return parseInt(localStorage.getItem('cartCount')) || 0;
}

updateCartBadge(getCartCount());

function getCartCount() {
    return parseInt(localStorage.getItem('cartCount')) || 0;
}

const container = document.querySelector('#cartContainer');
console.log(container);
function updateCartUI() {
    updateCartCounter(cart.length);
    updateCartTotal(calculateTotalCost()); 
}

function updateCartCounter(count) {
    const cartCounter = document.getElementById('cartCounter');
    if (cartCounter) {
        cartCounter.textContent = count;
    }
}

function updateCartTotal() {
    const totalCost = calculateTotal();
    console.log("Total Cost:", totalCost);
    const cartTotalElement = document.getElementById('cartTotal');
    if (cartTotalElement) {
        if (!isNaN(parseFloat(totalCost))) {
            console.log("Updating cart total:", '₹' + parseFloat(totalCost).toFixed(2));
            cartTotalElement.textContent = '₹' + parseFloat(totalCost).toFixed(2);
            console.log("Total Cost:", totalCost);
        } else {
            console.error('Invalid total cost:', totalCost);
        }
    } else {
        console.error('Cart total element not found.');
    }
}

updateCartCounter(1);
updateCartTotal(50);

function displayNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
}

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

const title = urlParams.get('title');
const price = urlParams.get('price');
const imageUrl = urlParams.get('imageUrl');

if (title && price && imageUrl) {
    cart.push({ title, price, imageUrl });
    displayCart();
}

createCards(cardData);
setupPagination();
