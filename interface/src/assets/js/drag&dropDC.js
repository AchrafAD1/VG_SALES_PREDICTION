var correctCards = 0;

requests = ['','','','','','','','','','','','','','','','','',''];

// Function to hide the success message
function hideSuccessMessage() {
  var successMessage = document.getElementById('successMessage');
  successMessage.style.display = 'none';
  successMessage.style.left = '580px';
  successMessage.style.top = '250px';
  successMessage.style.width = '0';
  successMessage.style.height = '0';
}
[{}]
reqChamps = ['Name', 'Year_of_Release', 'Genre', 'Publisher', 'MA_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
var numbers = ['SELECT', '*', 'FROM', 'GAMES', 'WHERE', 'MA_Sales != Null', '|', 'Critic_Score != Null', '|', 'Critic_Count != Null', '|', 'User_Score != Null', '|', 'User_Count != Null', '|', 'Developer != Null', '|', 'Rating != Null'
];
var reqPre = ['SELECT', '*', 'FROM', 'GAMES', 'WHERE', 'MA_Sales != Null', '|', 'Critic_Score != Null', '|', 'Critic_Count != Null', '|', 'User_Score != Null', '|', 'User_Count != Null', '|', 'Developer != Null', '|', 'Rating != Null'
];
// Function to initialize the game
function init() {
  // Hide the success message
  hideSuccessMessage();

  // Reset the game
  correctCards = 0;

  var cardPile = document.getElementById('cardPile');
  var cardSlots = document.getElementById('cardSlots');

  // Clear the cardPile and cardSlots elements
  cardPile.innerHTML = '';
  cardSlots.innerHTML = '';

  // Create the pile of shuffled cards
  numbers.sort(function () {
    return Math.random() - 0.5;
  });

  for (var i = 0; i < numbers.length; i++) {
    var card = document.createElement('div');
    card.textContent = numbers[i];
    card.dataset.number = numbers[i];
    addedVal = numbers[i]
    if (addedVal == '*') { addedVal = 'Etoile' }
    else if (addedVal == '|') { addedVal = 'Barre' }
    card.id = 'card' + addedVal;
    cardPile.appendChild(card);
    makeDraggable(card);
  }

  // Create the card slots 
  var words = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  for (var i = 1; i <= numbers.length; i++) {
    var slot = document.createElement('div');
    slot.textContent = i;
    slot.dataset.number = i;
    cardSlots.appendChild(slot);
    makeDroppable(slot);
  }
}

// Function to make a card draggable
function makeDraggable(card) {
  card.style.cursor = 'move';
  card.draggable = true;

  card.addEventListener('dragstart', function (event) {
    event.dataTransfer.setData('text/plain', event.target.dataset.number);
    console.log(event.target.dataset)
  });

  card.addEventListener('dragend', function (event) {
    // Handle drag end if needed
  });
}

// Function to make a slot droppable
function makeDroppable(slot) {
  slot.addEventListener('dragover', function (event) {
    event.preventDefault();
  });

  slot.addEventListener('drop', function (event) {
    event.preventDefault();
    var slotNumber = parseInt(event.target.dataset.number, 14);
    var cardNumber = event.dataTransfer.getData('text/plain');
    if (cardNumber == '*'){cardNumber = "Etoile"}
    else if (cardNumber == '|'){cardNumber = "Barre"}
    console.log(cardNumber)
    console.log(event.target.dataset.number)
    
      
      
        
      if (!isNaN(event.target.innerHTML)) {
        event.target.classList.add('correct');
        event.target.textContent = '';
        event.target.removeEventListener('dragover', null);
        event.target.removeEventListener('drop', null);
        // requests.push(cardNumber)
        requests[event.target.dataset.number-1] = cardNumber;

      
        event.target.appendChild(document.querySelector('#card' + cardNumber));
        console.log(document.querySelector('#card' + cardNumber))
        document.querySelector('#card' + cardNumber).style.position = 'relative';
        document.querySelector('#card' + cardNumber).style.left = '0';
        document.querySelector('#card' + cardNumber).style.top = '0';
        document.querySelector('#card' + cardNumber).style.cursor = 'pointer';
        document.querySelector('#card' + cardNumber).addEventListener('click', () => {
            requests[event.target.dataset.number-1] = '';
            event.target.classList.remove('correct');
            console.log(document.querySelector('#card' + cardNumber))
            cardPile.appendChild(document.querySelector('#card' + cardNumber));
            event.target.textContent = event.target.dataset.number.toString();
            document.querySelector('#card' + cardNumber).style.position = 'relative';
            document.querySelector('#card' + cardNumber).style.left = '0';
            document.querySelector('#card' + cardNumber).style.top = '0';
            document.querySelector('#card' + cardNumber).style.cursor = 'move';	

            document.querySelector('#card' + cardNumber).draggable = true;
        });

        document.querySelector('#card' + cardNumber).draggable = false;
        if(requests.length === numbers.length) {
            btn.style.cursor = 'pointer';
            btn.classList.remove('disabled');
        }

    }
});
}


btn.addEventListener('click', function(e) {
    console.log(requests);
    console.log(reqPre);
    if(!requests.includes('')) {
        found = 0
        this.style.cursor = 'pointer';
        this.classList.remove('disabled');
        for (var i = 0; i < requests.length; i++) {
            if ([1,2,3,4,5,6,7,8,9,10,11].includes(i)) {
                if(reqChamps.includes(requests[i])){
                    console.log(requests[i]);
                    found++
                }
            }
            
            else if (requests[i] == reqPre[i]){
                found++
            }
        }
        console.log(found);
        console.log(requests);
        console.log(reqPre);
        if(found == requests.length){
            fetch(`http://127.0.0.1:5000/get_data/missing_values`)
            .then(() =>  {
                showSuccessMessage();
            })
        }
    }
});

// Function to show the success message
function showSuccessMessage() {
  var successMessage = document.getElementById('successMessage');
  successMessage.style.display = 'block';
  successMessage.style.left = '380px';
  successMessage.style.top = '200px';
  successMessage.style.width = '400px';
  successMessage.style.height = '100px';
  successMessage.style.opacity = 1;
}

showDataBtn.onclick = () => location.href = 'data_cleaning.html';

// Initialize the game
init();
